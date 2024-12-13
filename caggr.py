from .ehandler import e_handler
from .install_module import packageinstaller

# [FUNCTION]
# notification/alert function
def notify():
    # update("answer", ""), update("ntfytt", ""), update("ntfyinfo", "")
    # talk(), notify()
    try:dur = int(data("notifdur"))
    except:dur = 5
    title = data("notifscap") + "\n" + data("ntfytt")
    info = data("ntfyinfo")
    try:droid.makeToast(str(title) + "\n" + str(info)), droid.vibrate()
    except:pass
    try:winsound.Beep(data("beepfreq"), data("beepdur"))
    except:
        try:pass # sys.stdout.write("a")
        except:pass
    try:
        notify2.init("Alert!")
        notif = notify2.Notification(str(title), str(info), icon = data("ntfyico"))
        # notif.set_urgency(notify2.URGENCY_CRITICAL)
        notif.show()
        notif.set_timeout(dur)#, time.sleep(60)
    except:pass