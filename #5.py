#5 Создайте класс Clock со статичным методом Say_time, который будет выводить на экран текущее время.
#Подсказка: для этого можете воспользоваться стандартной библиотекой time.
from time import localtime, time
class Clock:
  @staticmethod
  def Say_time():
    current_time = localtime(time())
    time_string = f'{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}'
    print("Current time:", time_string)
Clock.Say_time()