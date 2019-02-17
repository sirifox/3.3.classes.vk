import requests
import pprint


class VkUser:

    vk = 'https://api.vk.com/method/'
    token = 'some valid token'

    def __init__(self, us_id):
        self.us_id = us_id
        self.params = {
            'v': '5.92',
            'access_token': self.token
        }

    def __and__(self, other):
        us_params = self.params
        us_params.update({'target_uid': other.us_id})
        mut_friends = requests.get(self.vk + 'friends.getMutual', params=us_params).json()['response']
        user_list = []
        for friend in mut_friends:
            user_list.append(str(VkUser(friend)))
        return user_list

    def __str__(self):
        return 'https://vk.com/id' + str(self.us_id)

    def get_status(self):
        return requests.get(self.vk + 'status.get', params=self.params).json()

    def get_friends(self):
        return requests.get(self.vk + 'friends.get', params=self.params).json()


user1 = VkUser('some user_id')
user2 = VkUser('some user_id')

print(user1)
pprint.pprint(user1 & user2)
