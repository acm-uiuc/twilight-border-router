from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/v1/system/power')
def on_off():
    power_status = request.args.get('on', default=1, type=bool)
    return '', 200

@app.route('/v1/commands')
def change_mode():
    name = request.args.get('name', default='', type=str)[1:-1]

    if name == 'circadian':
        print('circadian')
    elif name[0:5] == 'color':
        print(name[5:])
    elif name == 'rain':
        print('rain')
    elif name == '':
        print('current mode')
    else:
        return '', 400
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)

