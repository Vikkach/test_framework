class UserDataChecker:
    def check_created_user(self, input_user_data, output_user_data):
        self.compare_user_names(input_user_data, output_user_data)
        self.compare_user_job(input_user_data, output_user_data)

    @staticmethod
    def compare_user_names(input_user_data, output_user_data):
        input_user_name = input_user_data.get('name')
        output_user_name = output_user_data.get('name')
        assert input_user_name == output_user_name, f'User was created with name {input_user_name} but got {output_user_name}'

    @staticmethod
    def compare_user_job(input_user_data, output_user_data):
        input_user_job = input_user_data.get('job')
        output_user_job = output_user_data.get('job')
        assert input_user_job == output_user_job, f'User was created with job {input_user_job} but got {output_user_job}'
