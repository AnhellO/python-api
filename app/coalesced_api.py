from flask import Flask, request, abort
from coalesce import AverageCoalesceConcreteStrategy, MaxCoalesceConcreteStrategy, MinCoalesceConcreteStrategy, CoalesceContext
import api

app = Flask(__name__)

APIS = [
    'http://0.0.0.0:5001',
    'http://0.0.0.0:5002',
    'http://0.0.0.0:5003',
]

@app.route('/')
def index():
    try:
        member_id = request.args.get("member_id")
        strategy = request.args.get("strategy")

        if member_id == None:
            return {}
        
        members = []
        for url in APIS:
            member = (api.API(url)).get_member(member_id)
            members.append(member)
        
        print(members)
        context = CoalesceContext(members, strategy)
        return context.execute_strategy()
    except Exception as e:
        print(e)
        abort(404)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)