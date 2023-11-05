def f(amount_to_pay):
        coin5=0
        coin2=0
        coin1=0
        coins=0
        while amount_to_pay>0:
            if amount_to_pay>=5:
                coin5+=1
                amount_to_pay-=5
            elif amount_to_pay>=2:
                coin2+=1
                amount_to_pay-=2
            elif amount_to_pay==1:
                coin1+=1
                amount_to_pay-=1
            coins+=1
        return coins
    
print(f(8))
