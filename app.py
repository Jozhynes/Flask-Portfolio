from flask import Flask,url_for,render_template,request

app=Flask(__name__)
Mylist=[]

@app.route('/')
def Home():
    
    return render_template('index.html',products=Mylist)


@app.route('/contacts')
def contact():
    return render_template('contact.html')

@app.route('/Products', methods=["POST", "GET"])
def product():
    if request.method == "POST":
        pname = request.form['pname']
        quantity = request.form['Quantity']
        price = request.form['Price']
        
        # Append dictionary to list
        Mylist.append({
            'Product_name': pname,
            'Quantity': quantity,
            'Price': price
        })
    print(Mylist)
    
        





if __name__=="__main__":
   app.run(debug=True)