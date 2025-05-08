document.addEventListener('DOMContentLoaded', function() {
    const amountInput = document.getElementById('amount');
    const calculateBtn = document.getElementById('calculate-btn');
    const resultsDiv = document.getElementById('results');
    const feeAmount = document.getElementById('fee-amount');
    const totalAmount = document.getElementById('total-amount');
    const receivingAmount = document.getElementById('receiving-amount');
    const proceedBtn = document.getElementById('proceed-btn');
    const cancelBtn = document.getElementById('cancel-btn');

    // Calculate button click handler
    calculateBtn.addEventListener('click', function() {
        const amount = amountInput.value;
        
        if (amount && parseFloat(amount) > 0) {
            fetch('/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `amount=${amount}`
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    feeAmount.textContent = data.fee_amount;
                    totalAmount.textContent = data.total_amount;
                    receivingAmount.textContent = data.receiving_amount;
                    resultsDiv.style.display = 'block';
                } else {
                    alert(data.message);
                    resultsDiv.style.display = 'none';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                resultsDiv.style.display = 'none';
            });
        } else {
            alert('Please enter a valid amount greater than 0');
            resultsDiv.style.display = 'none';
        }
    });

    // Proceed button click handler
    proceedBtn.addEventListener('click', function() {
        const amount = amountInput.value;
        if (amount && parseFloat(amount) > 0) {
            alert(`Proceeding with payment of ${totalAmount.textContent}`);
            // In real app, redirect to payment page
        } else {
            alert('Please calculate a valid amount first');
        }
    });

    // Cancel button click handler
    cancelBtn.addEventListener('click', function() {
        amountInput.value = '';
        feeAmount.textContent = '$0.00';
        totalAmount.textContent = '$0.00';
        receivingAmount.textContent = 'KES 0.00';  // Changed to KES
        resultsDiv.style.display = 'none';
    });

    // Allow Enter key to trigger calculation
    amountInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            calculateBtn.click();
        }
    });
});