# help:如何使用查询功能：
# action_data数组，['type'] == 4]判断条件和值，[["user_id", "sku_id"]]输出字段
# action_data[action_data['type'] == 4][["user_id", "sku_id"]]

b=[]
b[ 'attr1'],b[ 'attr2'],b[ 'attr3'],b[ 'cate'],b[ 'brand']=b['sku_id'],b['sku_id'],b['sku_id'],b['sku_id'],b['sku_id']

for i in b['sku_id']:
	b[ 'attr1'],b[ 'attr2'],b[ 'attr3'],b[ 'cate'],b[ 'brand']=c[c[ 'sku_id']==i][[ 'attr1', 'attr2', 'attr3', 'cate', 'brand']]