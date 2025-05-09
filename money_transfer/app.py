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
        
        # Validate amount is positive
        if user_amount <= 0:
            return jsonify({
                'success': False, 
                'message': 'Amount must be greater than zero',
                'show_results': False
            })
            
        # Calculations
        fee_amount = SENDING_FEES * user_amount
        amount_plus_fees = user_amount + fee_amount
        receiving_amount = EXCHANGE_RATE * user_amount

        return jsonify({
            'success': True,
            'fee_amount': "${:,.2f}".format(fee_amount),
            'total_amount': "${:,.2f}".format(amount_plus_fees),
            'receiving_amount': "KES {:,.2f}".format(receiving_amount),
            'show_results': True
        })
    except ValueError:
        return jsonify({
            'success': False, 
            'message': 'Please enter a valid number',
            'show_results': False
        })
    except Exception as e:
        return jsonify({
            'success': False, 
            'message': 'An unexpected error occurred',
            'show_results': False
        })

if __name__ == '__main__':
    app.run(debug=True)