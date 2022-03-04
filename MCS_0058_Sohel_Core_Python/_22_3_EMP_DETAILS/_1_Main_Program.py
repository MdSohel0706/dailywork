


from _22_3_EMP_DETAILS.controller.emp_controller import save_emp_data

if __name__ == '__main__':
    output = save_emp_data('in_emp_data.json')
    if output:
        print("***** Congratulations! Your registration completed ***** ")
        # return "Congratulations! Your signup completed"
    else:
        print("***** User already exists with this ID. ***** ")
        #return "Invalid login Attempt . Please provide valid credentials to prevent your login from being disabled."
