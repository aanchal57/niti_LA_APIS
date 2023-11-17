import requests

api_url = 'http://localhost:5000/api'  # Update with the correct URL when deploying to a real server

def check_credit_guarantee(applicant_name):
    # Simulate a Credit Guarantee API call
    response = requests.post(f'{api_url}/checkCreditGuarantee', json={
        'applicantName': applicant_name,
    },headers={'Content-Type': 'application/json'})
    if  response.json()['isEligible']:
        print("Applicants are eligible for credit Guarantee")
    return response.json()['isEligible']

def create_loan_application():
    applicant_name = 'John Doe'
    
    # Check Credit Guarantee eligibility
    is_eligible = check_credit_guarantee(applicant_name)

    if is_eligible:
        # Proceed with creating the loan application
        response = requests.post(f'{api_url}/createLoanApplication', json={
            'applicantName': applicant_name,
            'amount': 10000,
            'productId': '123',
            'creditGuaranteeEligibility': is_eligible,
        },headers={'Content-Type': 'application/json'})
        loan_application_id = response.json()['loanApplicationId']
        return loan_application_id
    else:
        print('Credit Guarantee not approved for the applicant.')
        return None

def auction_loan_application(loan_application_id):
    lenders = ['lender01', 'lender02']  # Add more lender IDs as needed
    all_offers = []

    # Send auction requests to all lenders
    
    for lender_id in lenders:
        response = requests.post(f'{api_url}/auctionLoanApplication', json={
            'loanApplicationId': loan_application_id,
            'productId': '123',
            'lenderId': lender_id,
        },headers={'Content-Type': 'application/json'})

        offer = response.json()
        all_offers.append(offer)
       # print(offer)

    # Display offers to the borrower and let them choose
    print('Received offers from lenders:')
    for idx, offer in enumerate(all_offers, start=1):
        print(f"{idx}. Lender: {offer['offer']['lenderId']}, Offer ID: {offer['offer']['offerId']}, Interest Rate: {offer['offer']['interestRate']}")

    # Let the borrower choose an offer (you can implement your logic here)
    chosen_offer_index = int(input('Borrower choose an offer by entering the corresponding number between 1 and 2: '))
    chosen_offer = all_offers[chosen_offer_index - 1]

    # Return the chosen offer ID
    print(chosen_offer)
    return chosen_offer['offer']['offerId']

def set_offer_response(offer_id):
    response = requests.post(f'{api_url}/setOfferResponse', json={
        'offerId': offer_id,
        'response': 'ACCEPTED',
    },headers={'Content-Type': 'application/json'})
    return response.json()

if __name__ == '__main__':
    # Loan Application Journey

    # Step 1: Check Credit Guarantee
    loan_application_id = create_loan_application()

    if loan_application_id:
        print(f'Crearting Loan application with Loan Application ID: {loan_application_id}')

        # Step 2: Auction Loan Application
        chosen_offer_id = auction_loan_application(loan_application_id)

        # Step 3: Set Offer Response
        set_offer_response(chosen_offer_id)
        print('Offer Response Set Successfully')
