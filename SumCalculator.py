import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="🔢 Sum Calculator Pro",
    page_icon="🔢",
    layout="wide"
)

# Custom CSS for attractive styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .result-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-size: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }
    
    .formula-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: white;
        text-align: center;
        font-size: 1.2rem;
    }
    
    .step-box {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        color: white;
        border-left: 4px solid #fff;
    }
    
    .current-calc {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
        font-weight: bold;
        color: #333;
    }
    
    .stats-box {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: #333;
        text-align: center;
    }
    
    .fun-fact {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        color: #333;
        border-left: 4px solid #667eea;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-size: 1.1rem;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        width: 100%;
    }
    
    .number-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(50px, 1fr));
        gap: 10px;
        margin: 1rem 0;
    }
    
    .number-item {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        animation: fadeIn 0.5s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🔢 Sum Calculator Pro</h1>
    <p>Calculate the sum of numbers from 1 to n with beautiful animations!</p>
</div>
""", unsafe_allow_html=True)

# Create sidebar for controls
with st.sidebar:
    st.markdown("### ⚙️ Controls")
    
    # Input for n
    n = st.number_input(
        "Enter the value of n:",
        min_value=1,
        max_value=100,
        value=10,
        step=1,
        help="Enter a positive integer (max 100 for visual display)"
    )
    
    # Animation speed
    animation_speed = st.select_slider(
        "Animation Speed:",
        options=["Slow", "Medium", "Fast", "Instant"],
        value="Medium",
        help="Choose how fast to show the calculation steps"
    )
    
    # Display options
    show_formula = st.checkbox("Show Mathematical Formula", value=True)
    show_steps = st.checkbox("Show Step-by-Step Calculation", value=True)
    show_numbers = st.checkbox("Show Number Grid", value=True)
    show_stats = st.checkbox("Show Statistics", value=True)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    if st.button("🚀 Calculate Sum Using Loop", key="calculate"):
        
        # Show formula if requested
        if show_formula:
            st.markdown(f"""
            <div class="formula-box">
                <h3>📚 Mathematical Formula</h3>
                <p><strong>Sum = n × (n + 1) ÷ 2</strong></p>
                <p>For n = {n}: Sum = {n} × {n+1} ÷ 2 = <strong>{n*(n+1)//2}</strong></p>
                <p>But we'll calculate it using a loop! 🔄</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Speed settings
        speed_map = {"Slow": 0.3, "Medium": 0.1, "Fast": 0.05, "Instant": 0}
        delay = speed_map[animation_speed]
        
        # Show number grid if requested
        if show_numbers and n <= 50:
            st.markdown("### 🔢 Numbers to Add:")
            numbers_html = '<div class="number-grid">'
            for i in range(1, n + 1):
                numbers_html += f'<div class="number-item">{i}</div>'
            numbers_html += '</div>'
            st.markdown(numbers_html, unsafe_allow_html=True)
            
            if delay > 0:
                time.sleep(1)
        
        # Main calculation section
        st.markdown("### 🔄 Loop Calculation in Progress...")
        
        # Create placeholders for dynamic content
        progress_container = st.container()
        current_calc_placeholder = st.empty()
        
        # Progress bar using Streamlit's built-in progress bar
        progress_bar = st.progress(0)
        
        # Initialize sum
        total_sum = 0
        calculation_steps = []
        
        # Perform loop calculation with animation
        for i in range(1, n + 1):
            total_sum += i
            
            # Store step for later display
            calculation_steps.append({
                'step': i,
                'number': i,
                'sum': total_sum,
                'equation': ' + '.join(map(str, range(1, i + 1)))
            })
            
            # Update progress bar
            progress = i / n
            progress_bar.progress(progress)
            
            # Show current calculation
            current_calc_placeholder.markdown(f"""
            <div class="current-calc">
                <h4>Step {i}: Adding {i}</h4>
                <p><strong>Equation:</strong> {' + '.join(map(str, range(1, i + 1)))}</p>
                <p><strong>Current Sum:</strong> {total_sum}</p>
                <p><strong>Progress:</strong> {i}/{n} ({progress*100:.1f}%)</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Add delay for animation
            if delay > 0:
                time.sleep(delay)
        
        # Clear progress bar
        progress_bar.empty()
        
        # Show final result
        st.markdown(f"""
        <div class="result-box">
            <h2>🎉 Final Result</h2>
            <h1>Sum of 1 to {n} = {total_sum}</h1>
            <p>Calculated using a loop with {n} iterations!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show detailed steps if requested
        if show_steps and n <= 20:
            st.markdown("### 📋 Detailed Step-by-Step Calculation:")
            
            for step in calculation_steps:
                st.markdown(f"""
                <div class="step-box">
                    <strong>Step {step['step']}:</strong> 
                    Adding {step['number']} → 
                    Sum = {step['equation']} = {step['sum']}
                </div>
                """, unsafe_allow_html=True)
        
        elif show_steps and n > 20:
            st.warning("📝 Step-by-step display is limited to n ≤ 20 for better performance!")
        
        # Show algorithm code
        with st.expander("🧠 View the Python Loop Code"):
            st.code("""
def calculate_sum_using_loop(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum

# Usage
result = calculate_sum_using_loop({})
print(f"Sum = {{result}}")
            """.format(n), language="python")

with col2:
    if show_stats:
        st.markdown("### 📊 Statistics")
        
        if n > 0:
            theoretical_sum = n * (n + 1) // 2
            average = theoretical_sum / n
            
            # Create statistics display
            st.markdown(f"""
            <div class="stats-box">
                <h4>📈 Key Statistics</h4>
                <p><strong>Input (n):</strong> {n}</p>
                <p><strong>Sum Result:</strong> {theoretical_sum}</p>
                <p><strong>Average:</strong> {average:.2f}</p>
                <p><strong>Loop Iterations:</strong> {n}</p>
                <p><strong>Number Type:</strong> {'Even' if n % 2 == 0 else 'Odd'}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Fun facts section
        st.markdown("### 🎭 Fun Facts")
        
        fun_facts = [
            f"🔺 The sum {n*(n+1)//2} is called a triangular number!",
            f"🧮 This formula was discovered by Gauss at age 10!",
            f"⚡ Formula method: O(1) vs Loop method: O(n)",
            f"🎯 The {n}th triangular number has {len(str(n*(n+1)//2))} digits",
            f"🔢 Sum of first {n} numbers = {n}th triangular number"
        ]
        
        for fact in fun_facts:
            st.markdown(f"""
            <div class="fun-fact">
                {fact}
            </div>
            """, unsafe_allow_html=True)

# Performance comparison section
st.markdown("---")
st.markdown("### ⚡ Performance Comparison")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="stats-box">
        <h4>🔄 Loop Method</h4>
        <p><strong>Algorithm:</strong> Iterative addition</p>
        <p><strong>Time Complexity:</strong> O(n)</p>
        <p><strong>Space Complexity:</strong> O(1)</p>
        <p><strong>Iterations:</strong> n times</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stats-box">
        <h4>⚡ Formula Method</h4>
        <p><strong>Algorithm:</strong> Direct calculation</p>
        <p><strong>Time Complexity:</strong> O(1)</p>
        <p><strong>Space Complexity:</strong> O(1)</p>
        <p><strong>Iterations:</strong> 1 time</p>
    </div>
    """, unsafe_allow_html=True)

# Educational section
with st.expander("🎓 Learn More About Sum Calculations"):
    st.markdown("""
    ### 🔢 Sum of Natural Numbers
    
    **What are we calculating?**
    - We're finding the sum: 1 + 2 + 3 + ... + n
    - This is called the sum of the first n natural numbers
    
    **Loop Approach (What this app does):**
    ```python
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    ```
    
    **Formula Approach (Gauss's Discovery):**
    ```python
    sum = n * (n + 1) // 2
    ```
    
    **Why does the formula work?**
    - Imagine pairing numbers: (1 + n), (2 + n-1), (3 + n-2), ...
    - Each pair sums to (n + 1)
    - There are n/2 pairs
    - So total = (n + 1) × (n/2) = n × (n + 1) / 2
    
    **Historical Note:**
    Young Carl Friedrich Gauss amazed his teacher by instantly calculating the sum of numbers 1 to 100 using this pattern!
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>🌟 Built with Streamlit & Python | Sum Calculator Pro 🌟</p>
    <p>Demonstrating loop-based calculation: Sum = 1 + 2 + 3 + ... + n</p>
</div>
""", unsafe_allow_html=True)