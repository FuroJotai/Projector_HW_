def is_admin(func):
    def wrapper(user_type):
        if user_type == 'admin':
            return func(user_type)
        else:
            raise ValueError("Acces denied")
            
    return wrapper

@is_admin
def show_customer_receipt(user_type: str):
    print("Access successfull")




show_customer_receipt('admin')
show_customer_receipt(user_type='user')



