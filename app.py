from flask import Flask,jsonify,abort,make_response,request

app=Flask(__name__)

trendlist=[
        {
            'id':1,
            'category':'Sarees',
            'url':'https://g3fashion.com/blog/fashion/top-trends-of-party-saree/'
        },
        {
            'id':2,
            'category':'kurtas',
            'url':'https://www.shauryasanadhya.com/blogs/news/2020-trends/kurta-s-style'
        },
        {
            'id':3,
            'category':'Footwear',
            'url':'https://www.ele.com/fashion/accesories/g30783601/fall-shoe-trends-2020/'
        
        },
        {
            'id':4,
            'category':'Jewellery',
            'url':'https://www.cosompolitan.com/style-beauty/fashion/g31025659/fall-jewelry-trends-2020/'
            }
            ]

@app.route('/Weather/api/v1.0/trendlist',methods=['GET'])
def get_trend():
    return jsonify({'trendlist':trendlist})


@app.route('/Weather/api/v1.0/trendlist/<int:trend_id>',methods=['GET'])
def get_trends(trend_id):
    trend=[trend for trend in trendlist if trend['id']==trend_id]
    if len(trend)==0:
        abort(404)
    return jsonify({'trend':trend[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not Found'}),404)

@app.route('/Weather/api/v1.0/trendlist',methods=['POST'])
def create_trend():
    if not request.json or not 'category' or not 'url' in request.json:
        abort(400)
    trend={
            'id':trendlist[-1]['id'] + 1,
            'category':request.json['category'],
            'url':request.json['url']
            }
    trendlist.append(trend)
    return jsonify({'trend':trend}),201

@app.route('/Weather/api/v1.0/trendlist/<int:trend_id>',methods=['DELETE'])
def delete_task(trend_id):
    trend=[trend for trend in trendlist if trend['id']==trend_id]
    if len(trend)==0:
        abort(404)
    trendlist.remove(trend[0])
    return jsonify({'result':True})

if __name__=='__main__':
    app.run(debug=True)
