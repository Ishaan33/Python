from win10toast import ToastNotifier
import time
time.sleep(5)
toast = ToastNotifier()
toast.show_toast("Notification",
"Hey Buddy , \n How are you? ", duration = 20)