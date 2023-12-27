import schedule
import time as tm
from datetime import time
from schedule import repeat, every

@repeat(every().second)
def tarefa():
    print("Amo minha namorada")

#schedule.every().second.until(time(14,22,40)).do(tarefa)
#schedule.every(10).weeks.do(tarefa)
#schedule.every().hour.at(":15").do(tarefa)

while True:
    schedule.run_pending()
    tm.sleep(1)
