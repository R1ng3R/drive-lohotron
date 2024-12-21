import os
from json import load
import zipfile
import perspective

from flask import Flask, render_template, request
from databaseload import  cur, con, add_cam, get_cams_list, get_cam_coords
from werkzeug.utils import secure_filename
app = Flask(__name__)

current_cam_index = -1
cam_list = []

@app.route('/')
def mainform():
  return render_template('mainform.html')

@app.route('/analise')
def analise():
  current_cam_index = 0
  html = ""
  for i in cam_list:
    if i[1]:
      html += f"<br> <h2>Камера {i[0]}</h2>"
      cam_number = i[0]
      files = os.listdir(f'static/unzip/RealTime.zip/RealTime/{cam_number}/RealTime')
      for j in files:
        perspective.perspective(f'static/unzip/RealTime.zip/RealTime/{cam_number}/RealTime/{j}', get_cam_coords(cam_number))
        html += f"<image src=static/images/perspectived/{j.split('.')[0] + 'ready.' + j.split('.')[1]}></image> <br>"
  return render_template('analize.html', data=html)

@app.route('/file_send', methods=['post'])
def get_files():
  request.files['json'].save(os.path.join('static/uploads', secure_filename(request.files['json'].filename)))
  request.files['RealPhotos'].save(os.path.join('static/uploads', secure_filename(request.files['RealPhotos'].filename)))
  request.files['AsiuddContent'].save(os.path.join('static/uploads', secure_filename(request.files['AsiuddContent'].filename)))
  with zipfile.ZipFile(os.path.join('static/uploads', secure_filename(request.files['RealPhotos'].filename)), 'r') as zip_ref:
    zip_ref.extractall(os.path.join('static/unzip', secure_filename(request.files['RealPhotos'].filename)))
  with zipfile.ZipFile(os.path.join('static/uploads', secure_filename(request.files['AsiuddContent'].filename)),
                       'r') as zip_ref:
    zip_ref.extractall(os.path.join('static/unzip', secure_filename(request.files['AsiuddContent'].filename)))
  cam_list = json_check(os.path.join('static/uploads', secure_filename(request.files['json'].filename)))
  return app.redirect('/status')



@app.route('/status')
def status():
  return render_template('status.html', data=cam_list)

@app.route('/points')
def points_set():
  global current_cam_index, cam_list
  while True:
      current_cam_index += 1
      print(cam_list[current_cam_index], len(cam_list))
      if current_cam_index < len(cam_list):
          if not cam_list[current_cam_index][1]:
              dir = f"static/unzip/RealTime.zip/RealTime/{cam_list[current_cam_index][0]}/RealTime"
              dir = dir + '/' + os.listdir(dir)[0]

              return render_template('points.html', photo=dir)
      else:
        return app.redirect('/')

@app.route('/point_fix', methods=['post'])
def point_fix():
  x1 = request.form.get('x1')
  x2 = request.form.get('x2')
  x3 = request.form.get('x3')
  x4 = request.form.get('x4')
  x5 = request.form.get('x5')
  x6 = request.form.get('x6')
  y1 = request.form.get('y1')
  y2 = request.form.get('y2')
  y3 = request.form.get('y3')
  y4 = request.form.get('y4')
  y5 = request.form.get('y5')
  y6 = request.form.get('y6')
  add_cam(x1, x2, x3, x4, x5, x6, y1, y2, y3, y4, y5, y6, cam_list[current_cam_index][0], cur, con)
  return app.redirect('/points')


def json_check(name):
  global cam_list
  json = load(open(name, 'r'))
  json_cam_list = []
  database_cam_list = get_cams_list()

  zip_cam_list = os.listdir('static/unzip/RealTime.zip/RealTime')

  for i in json:
      if i['num'] in zip_cam_list:
        json_cam_list.append([i['num'], i['num'] in database_cam_list and i['num'] in zip_cam_list, "color:#00ff00" if i['num'] in database_cam_list else ("color:#ff0000" if str(i['num']) in zip_cam_list else "color:#ffff00")])
  cam_list = json_cam_list
  print(cam_list)
  return json_cam_list



if __name__ == '__main__':
  app.run(debug=True)
