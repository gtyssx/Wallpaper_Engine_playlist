import os
import json

print('欢迎使用wallpaper本地1sp播放列表导出工具'
      '导出播放列表为m3u8格式'
      '输入地址范例：C:Program Files(x86)\Steam\steamapps\workshop\content\\431960')
data_dz = input('输入wallpaper文件地址：')
data_name = input('输入导出文件名')
f = os.listdir(data_dz)
fw = open('{}.m3u8'.format(data_name), 'w', encoding='utf-8')
fw.write('#EXTM3U8\n#EXTINF:-1,\n')
for i in f:
    data_pj = data_dz + '\\' + i
    ff = os.listdir(data_pj)
    with open('{}\\project.json'.format(data_pj), 'r', encoding='utf-8') as f_json:
        data_json = json.load(f_json)
        try:
            if data_json['contentrating'] == 'Mature':
                if 'mp4' in data_json['file']:
                    fw.write('{}\\{}\n'.format(data_pj, data_json['file']))
        except KeyError:
            try:
                data_json['visibility']
            except KeyError:
                if 'mp4' in data_json['file']:
                    fw.write('\\{}\n'.format(data_pj, data_json['file']))
fw.close()
print('完成')
