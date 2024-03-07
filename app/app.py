Here's an example of a Python Flask API code that implements the given user story:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/loan-eligibility', methods=['POST'])
def assess_loan_eligibility():
    data = request.get_json()

    # Check if all required documents are provided
    required_documents = ['identification', 'proof_of_income', 'credit_history', 'employment_details']
    if not all(doc in data for doc in required_documents):
        return jsonify({'error': 'Missing required documents'}), 400

    # Verify the provided documents
    is_documents_verified = verify_documents(data)

    if is_documents_verified:
        # Assess the applicant's eligibility
        is_eligible = assess_eligibility(data)

        # Generate a report
        report = generate_report(data, is_eligible)

        # Notify the bank employee
        notify_bank_employee(report)

        return jsonify(report)
    else:
        return jsonify({'error': 'Documents verification failed'}), 400

def verify_documents(data):
    # Implement document verification logic here
    # Return True if all documents are verified successfully, otherwise False
    return True

def assess_eligibility(data):
    # Implement loan eligibility assessment logic here
    # Return True if the applicant is eligible, otherwise False
    return True

def generate_report(data, is_eligible):
    # Generate a report indicating the applicant's eligibility status
    report = {
        'applicant_name': data['identification']['applicant_name'],
        'eligibility_status': 'Eligible' if is_eligible else 'Not Eligible'
    }
    return report

def notify_bank_employee(report):
    # Implement notification logic here
    # Notify the bank employee about the applicant's eligibility status
    pass

if __name__ == '__main__':
    app.run()
```

This code defines a Flask API with a single route `/loan-eligibility`. When a POST request is made to this route with the required documents in the request body, the API performs the following steps:

1. Checks if all required documents (identification, proof of income, credit history, and employment details) are provided.
2. Verifies the provided documents using the `verify_documents` function.
3. If the documents are verified successfully, the API assesses the applicant's eligibility using the `assess_eligibility` function.
4. Generates a report indicating the applicant's eligibility status using the `generate_report` function.
5. Notifies the bank employee about the applicant's eligibility status using the `notify_bank_employee` function.
6. Returns the generated report as a JSON response.

Please note that the implementation of the document verification and loan eligibility assessment logic is not provided in this code snippet. You will need to implement these functions according to your specific requirements and business rules.