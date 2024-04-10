from flask import Flask, request

app = Flask(__name__)

def fibonacci_series(n):
    """
    Generate Fibonacci series up to the nth term.
    
    Parameters:
        n (int): Number of terms in the Fibonacci series.
        
    Returns:
        str: Fibonacci series up to the nth term.
    """
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return ', '.join(map(str, fib_series))

@app.route('/', methods=['GET'])
def index():
    return """
    <form action="/fibonacci" method="get">
        <label for="number">Enter a number:</label>
        <input type="number" id="number" name="number" min="1" max="5">
        <button type="submit">Submit</button>
    </form>
    """

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci_series():
    try:
        number = int(request.args.get('number'))
        if number < 1:
            return 'Number must be greater than 0'
        elif number > 5:
            return 'Number must be less than or equal to 5'
        else:
            series = fibonacci_series(number)
            return f'Fibonacci series up to {number}th term: {series}'
    except ValueError:
        return 'Invalid input, please provide a valid number'

if __name__ == '__main__':
    app.run(debug=True)

