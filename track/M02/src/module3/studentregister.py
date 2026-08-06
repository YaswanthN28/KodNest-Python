registered=input()
fee_paid=input()
identify_verification=input()
check_status=input()
if registered == "Yes":
    if fee_paid == "Yes" and identify_verification == "Yes":
        if check_status == "Pass":
            print("Access Granted")
        else:
            print("Access Denied: System Check Failed")
    else:
        print("Access Denied: Verification Pending")
else:
    print("Access Denied: Registration Incomplete")