
#검증용 풀그림
from datetime import datetime
from pytz import timezone

current_time = datetime.now(timezone("GMT"))

print("검증코드를 사용한 현재 시간은 %d시 %d분 %d초 입니다."%(current_time.hour, current_time.minute, current_time.second))

import time
fseconds = time.time()
current_second = fseconds%60
fminutes = fseconds/60
current_minute = fminutes%60
fhours = fseconds/60/60
current_hour = fhours%24
print("time()을 사용한 현재 시간은", current_hour,"시",current_minute,"분",current_second,"초 입니다.")

