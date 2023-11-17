from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data
product = {
    'productId': '123',
    'productName': 'Sample Product',
}

lenders = [
    {'lenderId': 'lender01', 'name': 'Lender_1'},
    {'lenderId': 'lender02', 'name': 'Lender_2'},
]
loan_offers = []
# Mock Credit Guarantee Check
def check_credit_guarantee(applicant_name):
    # Simple implementation: Approve all applicants for credit guarantee
    return True

@app.route('/api/checkCreditGuarantee', methods=['GET','POST'])
def check_credit_guarantee_route():
    data = request.get_json()
    applicant_name = data.get('applicantName', '')

    # Check Credit Guarantee eligibility (use the actual implementation)
    is_eligible = check_credit_guarantee(applicant_name)

    return jsonify({'isEligible': is_eligible}), 200

@app.route('/api/createLoanApplication', methods=['GET','POST'])
def create_loan_application():
    data = request.json
    #print(f'Request Headers: {request.headers}')
    loan_application_id = 'loan123'  # Generate a unique ID in a real scenario
    return jsonify({'loanApplicationId': loan_application_id})

#auctionLoanApplication
@app.route('/api/auctionLoanApplication', methods=['GET','POST'])
def auction_loan_application():
    # data = request.json
    # auction_id = 'auction456'  # Generate a unique ID in a real scenario
    # return jsonify({'auctionId': auction_id})
    data = request.get_json()

    loan_application_id = data.get('loanApplicationId', '')
    product_id = data.get('productId', '')
    lender_id = data.get('lenderId', '')

    # Mock: Assume lenders generate offers with interest rates
    interest_rate = 5.0  # Mock interest rate, replace with your logic

    offer = {
        'loanApplicationId': loan_application_id,
        'productId': product_id,
        'lenderId': lender_id,
        'offerId': len(loan_offers) + 1,  # Generate a unique offer ID (you may need a more sophisticated ID generation)
        'interestRate': interest_rate,
    }
    print(loan_offers)
    loan_offers.append(offer)

    return jsonify({'message': 'Loan offer received successfully', 'offer': offer}), 200



@app.route('/api/setOfferResponse', methods=['POST'])
def set_offer_response():
    data = request.json
    return jsonify({'message': 'Offer response set successfully'})

if __name__ == '__main__':
    app.run(debug=True ,port=5000,use_reloader=False)
