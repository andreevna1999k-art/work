import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from prac_tpl import build_for
P,IM=build_for('consultant')
if __name__=='__main__':
    from mk import build
    open('/home/user/work/chinsolvency/consultant-insolventa-sprl.src.html','w',encoding='utf-8').write(build(P))
