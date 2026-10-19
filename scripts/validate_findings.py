#!/usr/bin/env python3
"""Validate audit structure only; never establishes security correctness."""
import json
import sys

def validate(data):
    errors=[]
    if not isinstance(data,dict):
        return ['root must be an object']
    if data.get('schema_version') != 1: errors.append('schema_version must be 1')
    scope=data.get('scope',{})
    if not isinstance(scope,dict): return errors+['scope must be an object']
    for key in ('repository','revision','date'):
        if not isinstance(scope.get(key),str) or not scope[key].strip(): errors.append('scope.'+key+' is required; use an explicit unavailable reason if needed')
    if scope.get('status') not in ('partial','completed'): errors.append('scope.status invalid')
    if not isinstance(scope.get('limitations'),list): errors.append('scope.limitations must be a list')
    findings=data.get('findings')
    if not isinstance(findings,list): return errors+['findings must be a list']
    seen=set()
    for i,f in enumerate(findings):
        label='finding '+str(i+1)
        if not isinstance(f,dict):
            errors.append(label+' must be an object'); continue
        for key in ('id','title','location','preconditions','flow','controls_checked','impact','evidence','validation','remediation','retest'):
            if not isinstance(f.get(key),str) or not f[key].strip(): errors.append(label+': '+key+' required as nonempty text')
        fid=f.get('id')
        if isinstance(fid,str):
            if fid in seen: errors.append(label+': duplicate id')
            seen.add(fid)
        for key,options in {'severity':('critical','high','medium','low','informational'),'confidence':('high','medium','low'),'evidence_status':('reproduced','code-confirmed','unverified')}.items():
            if f.get(key) not in options: errors.append(label+': invalid '+key)
        if f.get('evidence_status')=='unverified' and f.get('confidence')=='high': errors.append(label+': unverified cannot have high confidence')
    return errors

if __name__=='__main__':
    if len(sys.argv)!=2:
        print('Usage: validate_findings.py findings.json',file=sys.stderr); sys.exit(2)
    try:
        with open(sys.argv[1],encoding='utf-8') as stream: data=json.load(stream)
        errors=validate(data)
    except (OSError,ValueError):
        print('Cannot read valid JSON; file content withheld.',file=sys.stderr); sys.exit(2)
    if errors:
        for error in errors: print(error,file=sys.stderr)
        sys.exit(1)
    confirmed=sum(f['evidence_status']!='unverified' and f['severity']!='informational' for f in data['findings'])
    print(f'Structure valid. Confirmed non-informational entries: {confirmed}. Evidence correctness NOT verified.')
