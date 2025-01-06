
class Notification:
    def __init__(self,message):
        self.message = message
    def msgcost(self):
        return 2.0


class Email(Notification):

    def msgcost(self):
        base_cost = super().msgcost()
        count1 = len(self.message.split())
        tot_cost = base_cost + count1*1.0
        return tot_cost


class SMS(Notification):

    def msgcost(self):
        base_cost = super().msgcost()
        count2 = len(self.message)
        tot_cost = base_cost + count2 * 0.50
        return tot_cost


N = int(input())
notifications = []
for _ in range(N):
    parts = input().split(" ")
    notif_typ = parts[0]
    message = parts[1] if len(parts) > 1 else ""
    # print(notif_type, message)
    if notif_typ == "Email":
        notifications.append(Email(message))
    elif notif_typ == "SMS":
        notifications.append(SMS(message))


for noti in notifications:
    cost = noti.msgcost()
    print(f"{noti.__class__.__name__}: {cost:.2f}")




































