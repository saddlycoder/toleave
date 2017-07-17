# @author: vk.com/cm_3ky 

import vk_api 

whitelist = [, 137691354, 71927597] # сообщества, которые игнорируются. пример : 123456789

vk_session = vk_api.VkApi(token='TOKEN') 

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
