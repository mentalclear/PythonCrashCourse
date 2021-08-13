from users import Admin

superadmin = Admin('james', 'bond', 'agent007', 'jbond@m5.co.uk', 'guess')
superadmin.describe_user()

superadmin_privileges = ["can add post", "can delete post", "can edit post", "can ban user", "can create user"]

superadmin.privileges.privileges = superadmin_privileges
superadmin.privileges.show_privileges()
