from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    admin = {'name': 'meeee'}
    images = [
      {
        'hotel': {'name': 'Rancho Relaxo', 'city':'NotSpringfield'},
        'imglink': 'https://vignette.wikia.nocookie.net/simpsons/images/b/b3/Rancho_Relaxo.PNG/revision/latest?cb=20100801024654'
      },
      
      {
        'hotel': {'name': 'Stanley Hotel', 'city':'Something Shining'},
        'imglink': 'http://www.stanleyhotel.com/uploads/9/8/6/9/98696462/stanley-style-044_13_orig.jpg'
      }
      
    ]
    return render_template(
              'main.html',
              title='Main',
              images=images,
              admin=admin
            )