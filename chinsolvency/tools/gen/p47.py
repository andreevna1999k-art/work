import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from city_tpl import build_for
P,IM=build_for('bistrita')
if __name__=='__main__':
    from mk import build
    open('/home/user/work/chinsolvency/executari-bistrita.src.html','w',encoding='utf-8').write(build(P))
