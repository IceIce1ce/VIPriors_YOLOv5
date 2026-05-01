import os
import json

if os.path.exists('tmp'):
    os.remove('tmp')
else:
    os.mkdir('tmp')
root = 'data/DelftBikes/test'
imgs = list(sorted(os.listdir(root)))
json_data = json.load(open(os.path.join('data/DelftBikes/', 'fake_test_annotations.json')))
for idx in range(len(imgs)):
    img_path = os.path.join(root, imgs[idx])
    labels = json_data[imgs[idx]]
    with open('tmp/' + imgs[idx].replace('jpg', 'txt'), 'w') as f:
        for ind, i in enumerate(labels['parts'], 0):
            f.write(str(labels['parts'][i]['absolute_bounding_box']['left']) + ',' +
                    str(labels['parts'][i]['absolute_bounding_box']['top']) + ',' +
                    str(labels['parts'][i]['absolute_bounding_box']['width']) + ',' +
                    str(labels['parts'][i]['absolute_bounding_box']['height']) + ',' +
                    str(labels['parts'][i]['trust']) + ',' + str(ind + 1) + '\n')
