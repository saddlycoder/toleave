# @author: vk.com/id402825767

import vk_api 

whitelist = [13376988, 7192147597] # сообщества, которые игнорируются. пример : 123456789

try:
    vk_session = vk_api.VkApi(token='TOKEN')
except vk_api.VkAuthError as err:
    print(err)

vk = vk_session.get_api() 

gr = vk.groups.get() 
gr = gr['items'] 


glenght = len(gr) 

i = 0 
while i < glenght: 
    if(gr[i] in whitelist):
        gr.append(gr[i]) 
i+=1
vk.groups.leave(group_id=gr[i]) 
i+=1 
print 'Perfect!'
