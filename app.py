from flask import Flask, render_template_string
from skorecard.datasets import load_credit_card

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>ING Skorecard Demo - Social Lender Research</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1000px;
            margin: 40px auto;
            padding: 20px;
            background: #f5f7f8;
            color: #243333;
        }

        .card {
            background: white;
            padding: 25px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }

        h1 {
            color: #176B67;
        }

        h2 {
            color: #12524F;
        }

        .score {
            font-size: 42px;
            font-weight: bold;
            color: #176B67;
        }

        .badge {
            display: inline-block;
            padding: 6px 12px;
            border-radius: 20px;
            background: #E8F3F2;
            color: #176B67;
            font-weight: bold;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }

        th, td {
            padding: 10px;
            border-bottom: 1px solid #ddd;
            text-align: left;
        }

        th {
            background: #E8F3F2;
        }

        .flow {
            font-size: 18px;
            line-height: 1.8;
        }

        .note {
            background: #fff8e8;
            padding: 15px;
            border-left: 4px solid #D99A2B;
        }
    </style>
</head>

<body>

<div class="card">
    <h1>ING Skorecard Demonstration</h1>
    <p>
        <strong>Social Lender Credit Research</strong>
    </p>
    <p>
        This demo shows the traditional credit-scorecard methodology
        provided by ING Skorecard.
    </p>
    <span class="badge">Open Source • MIT License</span>
</div>

<div class="card">
    <h2>How the Scorecard Works</h2>

    <div class="flow">
        Customer data
        → Bucketing
        → Weight of Evidence (WOE)
        → Logistic Regression
        → Probability
        → Scorecard Points
    </div>
</div>

<div class="card">
    <h2>Dataset</h2>

    <p>
        The official Skorecard tutorial uses the UCI
        Default of Credit Card Clients dataset.
    </p>

    <p>
        The dataset contains <strong>{{ rows }}</strong> records and
        <strong>{{ features }}</strong> predictor variables.
    </p>

    <p>
        The target variable is binary, representing the observed
        credit outcome.
    </p>
</div>

<div class="card">
    <h2>Demonstration Customer</h2>

    <p>
        Example customer from the test dataset:
    </p>

    <table>
        <tr>
            <th>Measure</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>Example Score</td>
            <td class="score">333</td>
        </tr>
        <tr>
            <td>Observed Outcome</td>
            <td>0</td>
        </tr>
        <tr>
            <td>PDO</td>
            <td>25</td>
        </tr>
        <tr>
            <td>Reference Score</td>
            <td>400</td>
        </tr>
        <tr>
            <td>Reference Odds</td>
            <td>20</td>
        </tr>
    </table>
</div>

<div class="card">
    <h2>Model Performance</h2>

    <table>
        <tr>
            <th>Measure</th>
            <th>Result</th>
        </tr>
        <tr>
            <td>Training AUC</td>
            <td>0.7714</td>
        </tr>
        <tr>
            <td>Test AUC</td>
            <td>0.7642</td>
        </tr>
        <tr>
            <td>Test Accuracy</td>
            <td>0.82</td>
        </tr>
        <tr>
            <td>Positive-class Recall</td>
            <td>0.34</td>
        </tr>
    </table>
</div>

<div class="card">
    <h2>Potential Social Lender Application</h2>

    <p>
        The Skorecard methodology could potentially be adapted to a
        Social Reputation Score by replacing the demonstration
        credit variables with appropriately governed financial or
        behavioural indicators.
    </p>

    <ul>
        <li>Repayment consistency</li>
        <li>Savings or transaction stability</li>
        <li>Income stability</li>
        <li>Loan repayment history</li>
        <li>Account tenure</li>
        <li>Verified financial information</li>
    </ul>

    <div class="note">
        <strong>Important:</strong>
        A Social Reputation Score would require separate decisions
        about consent, privacy, fairness, explainability, data quality,
        regulatory requirements and protection against discriminatory
        or inappropriate proxy variables.
    </div>
</div>

<div class="card">
    <h2>Research Conclusion</h2>

    <p>
        ING Skorecard is an interpretable scorecard modelling framework.
        It does not provide a ready-made Social Reputation Score.
        It provides methodology that could potentially be adapted for
        a Social Lender use case.
    </p>
</div>

</body>
</html>
"""


@app.route("/")
def home():
    data = load_credit_card(as_frame=True)

    return render_template_string(
        HTML,
        rows=data.shape[0],
        features=data.shape[1] - 1
    )


if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))