from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Updated Configuration
SENDING_FEES = 0.02
EXCHANGE_RATE = 128  # Changed to 128 KES per USD

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        user_amount = float(request.form['amount'])
        
        # Calculations
        fee_amount = SENDING_FEES * user_amount
        amount_plus_fees = user_amount + fee_amount
        receiving_amount = EXCHANGE_RATE * user_amount

        return jsonify({
            'success': True,
            'fee_amount': f"${fee_amount:,.2f}",
            'total_amount': f"${amount_plus_fees:,.2f}",
            'receiving_amount': f"KES {receiving_amount:,.2f}",  # Changed to KES
            'show_results': True
        })
    except ValueError:
        return jsonify({
            'success': False, 
            'message': 'Please enter a valid amount',
            'show_results': False
        })

if __name__ == '__main__':
    app.run(debug=True)