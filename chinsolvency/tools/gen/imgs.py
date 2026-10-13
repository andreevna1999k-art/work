# usage: python3 imgs.py NN  -> renders IM images of pNN.py to /tmp/imgNN and uploads them to WP media (prints ids)
import sys,os,importlib,subprocess
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import igx
n=sys.argv[1]; M=importlib.import_module('p'+n)
IMGS={k:(v[0],v[1],v[2],v[3]) for k,v in M.IM.items()}
out=f'/tmp/img{n}'; igx.render_d(IMGS,out)
S='/tmp/claude-0/-home-user-work/057d374e-6f74-511c-a2f4-1bfe9640b1d5/scratchpad'
for k,v in M.IM.items():
    r=subprocess.run(['bash',f'{S}/upimg.sh',f'{out}/{k}.webp',v[4],v[1]],capture_output=True,text=True,cwd=S)
    print(k,r.stdout.strip().split('\n')[0][:60])
