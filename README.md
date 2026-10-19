# Kira Security Audit

Kanıta dayalı web güvenlik incelemesi ve Türkçe raporlama için Claude Code / Agent Skills paketi.

## Ne yapar?

Kapsam ve endpoint envanteri çıkarır, güven sınırlarını belirler, kod akışını uçtan uca inceler, aday bulguları doğrular ve düzeltme önceliklerini raporlar.

- Kimlik doğrulama, oturum ve yetkilendirme
- IDOR/BOLA, tenant izolasyonu ve hassas veri erişimi
- Injection, XSS, SSRF, dosya yükleme ve API güvenliği
- Ödeme/webhook, eşzamanlılık ve iş mantığı
- Bağımlılıklar, CI/CD ve dağıtım yapılandırması
- Next.js, Node.js, Prisma ve Supabase için ek kontroller

## Claude Code kurulumu

Projenin ana klasöründe çalıştırın:

```bash
mkdir -p .claude/skills
git clone https://github.com/ankaroni/Kira-security-audit.git .claude/skills/kira-security-audit
```

Bu hedef klasör zaten varsa üzerine kopyalamayın; mevcut sürümü inceleyin.
Ardından Claude Code içinde:

```text
/kira-security-audit
```

Örnek istek:

> Bu projenin web güvenliğini kapsamlı incele. Uygulama kodunu değiştirme.
> İncelenen ve incelenmeyen alanları göster. Kanıtlanmış bulguları
> doğrulanamayan şüphelerden ayır. Türkçe rapor üret.

Depo adı Kira Security Audit; skill komutunun adı `kira-security-audit`.
`agents/openai.yaml` diğer uyumlu istemciler için arayüz metadatasıdır; Claude Code kurulumu için zorunlu değildir.

## İş akışı

1. Kapsam, yetkiler ve ortam sınırları
2. Mimari, endpoint envanteri ve tehdit modeli
3. Öncelikli uçtan uca kod incelemesi
4. Aday bulguların doğrulanması ve yanlış pozitif kontrolü
5. Etki/güven değerlendirmesi ve düzeltme önerileri
6. Raporlama, kapsam mutabakatı ve yeniden test planı

## Çıktılar

| Dosya | İçerik |
|---|---|
| `report.md` | Yönetici özeti, kanıtlar, önem dereceleri ve düzeltme planı |
| `findings.json` | Makine tarafından işlenebilir bulgular |
| `coverage.md` | İncelenen, test edilen, engellenen ve incelenmeyen alanlar |

Kanıt durumları: **reproduced** (testle), **code-confirmed** (tam kod akışıyla), **unverified** (henüz doğrulanmadı).
Şüpheler ve güçlendirme önerileri doğrulanmış güvenlik açığı toplamına dahil edilmez.

## Paket yapısı

- `SKILL.md`: ana iş akışı
- `references/`: kontrol listeleri, kanıt/önem kuralları, teknoloji notları ve değerlendirme senaryoları
- `assets/`: rapor ve JSON şablonları
- `scripts/validate_findings.py`: Python 3 ile rapor yapısı doğrulama
- `agents/`: uyumlu istemciler için metadata

```bash
python3 .claude/skills/kira-security-audit/scripts/validate_findings.py security-audit/WORK_RUN/findings.json
```

`WORK_RUN` yerine gerçek çıktı klasörünü kullanın. Boş şablon tamamlanmış rapor değildir; kapsam alanları doldurulmadan doğrulamadan geçmez.

## Sınırlar ve doğrulama

Bu paket bir çalışma yöntemi ve yardımcı doğrulayıcıdır; bağımsız bir güvenlik tarayıcısı değildir. Sonuçlar kullanılan model, araçlar, kaynak erişimi ve inceleme kapsamına bağlıdır. Hiçbir açık bulunmaması sistemin güvenli olduğunu kanıtlamaz.

Varsayılan olarak kodu inceleyip raporlar; uygulama kodunu değiştirmez. Aktif ağ testleri için ayrıca açık hedef/ortam kapsamı gerekir. Üretim verileri ve gerçek kullanıcı bilgileri doğrulama amacıyla kullanılmaz. Talimatlar teknik bir sandbox sağlamaz; araç izinleri ayrıca yönetilmelidir.

İlk kontrolde JSON doğrulayıcısının altı durumu sınandı. Küçük sentetik kaynak örneğinde eksik sahiplik kontrolü tespit edildi, korunan endpoint için eşdeğer bir açık raporlanmadı ve yapılmayan çalışma zamanı testi yapılmış gösterilmedi. Bu sınırlı kontrol, geniş bir güvenlik benchmark'ı veya gerçek site denetimi değildir.

Oluşturulan raporlar hassas bulgular içerebilir; bu depo yalnızca skill paketini dağıtır. Projelerinizdeki gerçek denetim raporlarını paylaşmadan önce gözden geçirin.
