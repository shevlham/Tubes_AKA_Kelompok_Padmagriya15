import streamlit as st
import time
import random
import string
from typing import List, Tuple
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="Perbandingan Algoritma Palindrome",
    page_icon="🔄",
    layout="wide"
)

st.markdown("""
<style>
    /* Main background with vibrant teal gradient */
    .main {
        background: linear-gradient(120deg, #070F2B 0%, #1B1A55 50%, #070F2B 100%);
        animation: gradientShift 8s ease infinite;
    }
    .stApp {
        background: linear-gradient(120deg, #070F2B 0%, #1B1A55 50%, #070F2B 100%);
        animation: gradientShift 8s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { filter: hue-rotate(0deg); }
        50% { filter: hue-rotate(10deg); }
        100% { filter: hue-rotate(0deg); }
    }
    
    /* Typography with modern look */
    h1 {
        color: #ffffff !important;
        font-weight: 900 !important;
        text-align: center;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
        padding: 30px 0 10px 0;
        font-size: 3rem !important;
        letter-spacing: -1px;
    }
    h2, h3 {
        color: #ffffff !important;
        font-weight: 800 !important;
    }
    h4, h5, h6, p, label, .stMarkdown {
        color: #f0fdfa !important;
    }
    
    /* Sidebar with dark emerald theme */
    [data-testid="stSidebar"] {
        background: #070F2B;
        border-right: 3px solid #10b981;
    }
    
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #d1fae5 !important;
    }
    
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
        color: #a7f3d0 !important;
    }
    
    /* Status boxes with modern neon effect */
    .status-box {
        padding: 28px;
        border-radius: 20px;
        margin: 16px 0;
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(16px);
        border: 3px solid rgba(255, 255, 255, 0.25);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.25),
                    inset 0 1px 1px rgba(255, 255, 255, 0.3);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .status-box::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
        transform: rotate(45deg);
        animation: shine 3s infinite;
    }
    
    @keyframes shine {
        0%, 100% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        50% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
    
    .status-box:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.3),
                    inset 0 1px 1px rgba(255, 255, 255, 0.4);
    }
    
    .iterative-box {
        border-color: #22d3ee;
        background: linear-gradient(135deg, rgba(6, 182, 212, 0.25) 0%, rgba(14, 165, 233, 0.15) 100%);
    }
    .recursive-box {
        border-color: #a78bfa;
        background: linear-gradient(135deg, rgba(167, 139, 250, 0.25) 0%, rgba(139, 92, 246, 0.15) 100%);
    }
    
    /* Character display with futuristic monospace look */
    .char-display {
        font-family: 'Courier New', 'SF Mono', 'Monaco', monospace;
        font-size: 22px;
        letter-spacing: 10px;
        padding: 24px;
        background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 100%);
        border-radius: 16px;
        margin: 20px 0;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15),
                    inset 0 2px 4px rgba(14, 165, 233, 0.1);
        text-align: center;
        font-weight: 700;
        border: 2px solid rgba(6, 182, 212, 0.3);
    }
    
    /* Stat cards with neon glow effect */
    .stat-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.18) 0%, rgba(255, 255, 255, 0.08) 100%);
        backdrop-filter: blur(12px);
        padding: 24px;
        border-radius: 20px;
        border: 2px solid rgba(255, 255, 255, 0.35);
        margin: 12px 0;
        box-shadow: 0 10px 24px rgba(0, 0, 0, 0.15),
                    0 0 20px rgba(6, 182, 212, 0.2);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
    }
    
    .stat-card:hover {
        transform: translateY(-6px) scale(1.03);
        box-shadow: 0 16px 32px rgba(0, 0, 0, 0.2),
                    0 0 30px rgba(6, 182, 212, 0.4);
        border-color: rgba(34, 211, 238, 0.6);
    }
    
    .stat-label {
        color: #ccfbf1;
        font-size: 12px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 10px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    
    .stat-value {
        color: #ffffff;
        font-size: 36px;
        font-weight: 900;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.3);
        letter-spacing: -1px;
    }
    
    /* Algorithm header with glowing effect */
    .algo-header {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.25) 0%, rgba(255, 255, 255, 0.15) 100%);
        backdrop-filter: blur(12px);
        padding: 20px;
        border-radius: 16px;
        border: 3px solid rgba(255, 255, 255, 0.4);
        margin-bottom: 20px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15),
                    0 0 25px rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .algo-header:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 28px rgba(0, 0, 0, 0.2),
                    0 0 35px rgba(255, 255, 255, 0.15);
    }
    
    /* Button with neon effect */
    .stButton > button {
        background: linear-gradient(135deg, #f59e0b 0%, #f97316 100%);
        color: white;
        font-weight: 800;
        border-radius: 16px;
        padding: 14px 28px;
        border: none;
        box-shadow: 0 6px 16px rgba(245, 158, 11, 0.5),
                    0 0 20px rgba(249, 115, 22, 0.3);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        font-size: 16px;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 10px 24px rgba(245, 158, 11, 0.6),
                    0 0 30px rgba(249, 115, 22, 0.5);
        background: linear-gradient(135deg, #fbbf24 0%, #fb923c 100%);
    }
    
    /* Progress bar with glow */
    .stProgress > div > div {
        background: linear-gradient(90deg, #f59e0b 0%, #f97316 100%);
        box-shadow: 0 0 15px rgba(245, 158, 11, 0.6);
    }
    
    /* Conclusion box with premium look */
    .conclusion-box {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.2) 0%, rgba(255, 255, 255, 0.1) 100%);
        backdrop-filter: blur(16px);
        padding: 28px;
        border-radius: 20px;
        border: 3px solid rgba(255, 255, 255, 0.35);
        margin: 24px 0;
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.2);
    }
    
    /* DataTable with modern styling */
    .stDataFrame {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
    }
    
    /* Sidebar button styling */
    [data-testid="stSidebar"] .stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);
    }
    
    [data-testid="stSidebar"] .stButton > button:hover {
        background: linear-gradient(135deg, #34d399 0%, #10b981 100%);
        box-shadow: 0 6px 16px rgba(16, 185, 129, 0.6);
    }
</style>
""", unsafe_allow_html=True)

class PalindromeChecker:
    def __init__(self):
        self.reset_stats()
    
    def reset_stats(self):
        self.iterative_comparisons = 0
        self.recursive_comparisons = 0
        self.recursive_depth = 0
        self.max_recursive_depth = 0
    
    def check_iterative(self, text: str, visualize_callback=None) -> Tuple[bool, List[Tuple[int, int]]]:
        """Algoritma Iteratif untuk pengecekan palindrome"""
        self.iterative_comparisons = 0
        steps = []
        left = 0
        right = len(text) - 1
        
        while left < right:
            steps.append((left, right))
            self.iterative_comparisons += 1
            
            if visualize_callback:
                visualize_callback(left, right, text)
            
            if text[left] != text[right]:
                return False, steps
            
            left += 1
            right -= 1
        
        return True, steps
    
    def check_recursive(self, text: str, left: int = 0, right: int = None, 
                       visualize_callback=None, steps: List = None) -> Tuple[bool, List[Tuple[int, int]]]:
        """Algoritma Rekursif untuk pengecekan palindrome"""
        if steps is None:
            steps = []
            self.recursive_comparisons = 0
            self.recursive_depth = 0
            self.max_recursive_depth = 0
        
        if right is None:
            right = len(text) - 1
        
        self.recursive_depth += 1
        self.max_recursive_depth = max(self.max_recursive_depth, self.recursive_depth)
        
        # Base case
        if left >= right:
            self.recursive_depth -= 1
            return True, steps
        
        steps.append((left, right))
        self.recursive_comparisons += 1
        
        if visualize_callback:
            visualize_callback(left, right, text)
        
        # Recursive case
        if text[left] != text[right]:
            self.recursive_depth -= 1
            return False, steps
        
        result, steps = self.check_recursive(text, left + 1, right - 1, visualize_callback, steps)
        self.recursive_depth -= 1
        return result, steps

def generate_palindrome(size: int, order: str) -> str:
    """Generate palindrome berdasarkan ukuran dan urutan"""
    if size < 3:
        size = 3
    
    # Buat setengah pertama
    half_size = size // 2
    
    if order == "Ascending":
        # Generate karakter ascending
        if half_size <= 26:
            first_half = string.ascii_lowercase[:half_size]
        else:
            # Untuk ukuran besar, ulangi alphabet
            repeats = (half_size // 26) + 1
            extended = (string.ascii_lowercase * repeats)[:half_size]
            first_half = extended
    else:  # Descending
        # Generate karakter descending
        if half_size <= 26:
            first_half = string.ascii_lowercase[half_size-1::-1]
        else:
            repeats = (half_size // 26) + 1
            extended = (string.ascii_lowercase * repeats)[:half_size]
            first_half = extended[::-1]
    
    # Buat palindrome
    if size % 2 == 0:
        # Genap: mirror tanpa karakter tengah
        palindrome = first_half + first_half[::-1]
    else:
        # Ganjil: tambah karakter tengah
        middle_char = 'x'
        palindrome = first_half + middle_char + first_half[::-1]
    
    return palindrome

def generate_random_palindrome(size: int) -> str:
    """Generate palindrome random"""
    if size < 3:
        size = 3
    
    half_size = size // 2
    
    # Generate setengah pertama secara random
    first_half = ''.join(random.choices(string.ascii_lowercase, k=half_size))
    
    # Buat palindrome
    if size % 2 == 0:
        palindrome = first_half + first_half[::-1]
    else:
        middle_char = random.choice(string.ascii_lowercase)
        palindrome = first_half + middle_char + first_half[::-1]
    
    return palindrome

def visualize_string(text: str, active_indices: Tuple[int, int] = None, 
                    color: str = "#3b82f6") -> str:
    """Membuat visualisasi string dengan highlight"""
    html = '<div class="char-display">'
    for i, char in enumerate(text):
        if active_indices and i in active_indices:
            bg_color = "#fbbf24" if color == "#3b82f6" else "#c084fc"
            html += f'<span style="color: #1f2937; background-color: {bg_color}; padding: 8px 12px; border-radius: 8px; font-weight: 800; display: inline-block; margin: 0 2px;">{char}</span>'
        else:
            html += f'<span style="color: #94a3b8; display: inline-block; margin: 0 2px;">{char}</span>'
    html += '</div>'
    return html

def main():
    st.title("Perbandingan Efisiensi Algoritma")
    st.markdown("<h3 style='text-align: center; color: #f1f5f9; font-weight: 600; margin-top: -10px;'>Validasi Palindrome: Iteratif vs Rekursif</h3>", unsafe_allow_html=True)
    
    # Sidebar untuk kontrol
    st.sidebar.markdown("<h2 style='color: #d1fae5;'>⚙️ Pengaturan</h2>", unsafe_allow_html=True)
    
    # Ukuran data
    data_size = st.sidebar.slider(
        "Ukuran Data (jumlah karakter)",
        min_value=3,
        max_value=1000,
        value=10,
        step=1
    )
    
    dataset_type = st.sidebar.radio(
        "Tipe Dataset",
        options=["Palindrome Pattern", "Palindrome Random", "Input Kustom"],
        index=0
    )
    
    # Urutan data (hanya untuk Palindrome Pattern)
    data_order = None
    if dataset_type == "Palindrome Pattern":
        data_order = st.sidebar.radio(
            "Urutan Karakter",
            options=["Ascending", "Descending"],
            index=0
        )
    
    # Kecepatan simulasi
    speed = st.sidebar.slider(
        "Kecepatan Simulasi (ms)",
        min_value=1,
        max_value=2000,
        value=500,
        step=1
    )
    
    custom_input = ""
    if dataset_type == "Input Kustom":
        custom_input = st.sidebar.text_input("Masukkan teks:", value="racecar")
        test_data = custom_input.lower()
    elif dataset_type == "Palindrome Random":
        # Tombol untuk regenerate
        if st.sidebar.button("Generate Palindrome Baru"):
            st.session_state.random_palindrome = generate_random_palindrome(data_size)
        
        if 'random_palindrome' not in st.session_state:
            st.session_state.random_palindrome = generate_random_palindrome(data_size)
        
        # Update jika ukuran berubah
        if len(st.session_state.random_palindrome) != data_size:
            st.session_state.random_palindrome = generate_random_palindrome(data_size)
            
        test_data = st.session_state.random_palindrome
    else:  # Palindrome Pattern - default
        test_data = generate_palindrome(data_size, data_order)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Data yang digunakan:**")
    st.sidebar.code(test_data[:50] + ("..." if len(test_data) > 50 else ""))
    st.sidebar.markdown(f"Panjang: {len(test_data)} karakter")
    
    is_valid_palindrome = test_data == test_data[::-1]
    if is_valid_palindrome:
        st.sidebar.success("Data adalah PALINDROME yang valid")
    else:
        st.sidebar.warning("Data BUKAN palindrome")
    
    # Tombol mulai simulasi
    if st.sidebar.button("Mulai Simulasi", type="primary", use_container_width=True):
        run_simulation(test_data, speed)

def run_simulation(test_data: str, speed: float):
    """Menjalankan simulasi perbandingan algoritma"""
    checker = PalindromeChecker()
    speed_sec = speed / 1000.0
    
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Container untuk visualisasi
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="algo-header">
            <h2 style='margin: 0; color: #22d3ee;'>Algoritma Iteratif</h2>
            <p style='margin: 5px 0 0 0; font-size: 14px; color: #a7f3d0;'>Algoritma berdasarkan Iteratif</p>
        </div>
        """, unsafe_allow_html=True)
        iterative_viz = st.empty()
        iterative_status = st.empty()
    
    with col2:
        st.markdown("""
        <div class="algo-header">
            <h2 style='margin: 0; color: #a78bfa;'>Algoritma Rekursif</h2>
            <p style='margin: 5px 0 0 0; font-size: 14px; color: #a7f3d0;'>Algoritma berdasarkan pemanggilan fungsi dirinya sendiri</p>
        </div>
        """, unsafe_allow_html=True)
        recursive_viz = st.empty()
        recursive_status = st.empty()
    
    # Progress bars
    progress_col1, progress_col2 = st.columns(2)
    with progress_col1:
        iter_progress = st.progress(0)
    with progress_col2:
        rec_progress = st.progress(0)
    
    # Jalankan iteratif
    start_time_iter = time.time()
    
    def iterative_callback(left, right, text):
        iterative_viz.markdown(
            visualize_string(text, (left, right), "#3b82f6"),
            unsafe_allow_html=True
        )
        iterative_status.markdown(f"""
        <div class="status-box iterative-box">
            <p style='font-size: 16px; margin: 8px 0;'><strong>Posisi:</strong> {left} ('{text[left]}') ⟷ {right} ('{text[right]}')</p>
            <p style='font-size: 16px; margin: 8px 0;'><strong>Perbandingan:</strong> {checker.iterative_comparisons}</p>
        </div>
        """, unsafe_allow_html=True)
        progress = min((checker.iterative_comparisons / (len(test_data) // 2 + 1)), 1.0)
        iter_progress.progress(progress)
        time.sleep(speed_sec)
    
    is_palindrome_iter, iter_steps = checker.check_iterative(test_data, iterative_callback)
    time_iter = time.time() - start_time_iter
    
    iterative_status.markdown(f"""
    <div class="status-box iterative-box">
        <p style='font-size: 18px; font-weight: 700; margin: 8px 0;'>Selesai!</p>
        <p style='font-size: 16px; margin: 8px 0;'><strong>Hasil:</strong> <span style='color: #fbbf24; font-weight: 800;'>{'PALINDROME ' if is_palindrome_iter else 'BUKAN PALINDROME ✗'}</span></p>
    </div>
    """, unsafe_allow_html=True)
    iter_progress.progress(1.0)
    
    # Jalankan rekursif
    start_time_rec = time.time()
    
    def recursive_callback(left, right, text):
        recursive_viz.markdown(
            visualize_string(text, (left, right), "#8b5cf6"),
            unsafe_allow_html=True
        )
        recursive_status.markdown(f"""
        <div class="status-box recursive-box">
            <p style='font-size: 16px; margin: 8px 0;'><strong>Posisi:</strong> {left} ('{text[left]}') ⟷ {right} ('{text[right]}')</p>
            <p style='font-size: 16px; margin: 8px 0;'><strong>Perbandingan:</strong> {checker.recursive_comparisons}</p>
            <p style='font-size: 16px; margin: 8px 0;'><strong>Kedalaman Rekursi:</strong> {checker.recursive_depth}</p>
        </div>
        """, unsafe_allow_html=True)
        progress = min((checker.recursive_comparisons / (len(test_data) // 2 + 1)), 1.0)
        rec_progress.progress(progress)
        time.sleep(speed_sec)
    
    is_palindrome_rec, rec_steps = checker.check_recursive(test_data, visualize_callback=recursive_callback)
    time_rec = time.time() - start_time_rec
    
    recursive_status.markdown(f"""
    <div class="status-box recursive-box">
        <p style='font-size: 18px; font-weight: 700; margin: 8px 0;'>Selesai!</p>
        <p style='font-size: 16px; margin: 8px 0;'><strong>Hasil:</strong> <span style='color: #fbbf24; font-weight: 800;'>{'PALINDROME ' if is_palindrome_rec else 'BUKAN PALINDROME ✗'}</span></p>
    </div>
    """, unsafe_allow_html=True)
    rec_progress.progress(1.0)
    
    # Tampilkan statistik
    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>Hasil Perbandingan</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    stat_col1, stat_col2, stat_col3 = st.columns(3)
    
    with stat_col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-label">⏱Waktu Iteratif</div>
            <div class="stat-value">{:.4f}s</div>
        </div>
        """.format(time_iter), unsafe_allow_html=True)
        
        st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Perbandingan Iteratif</div>
            <div class="stat-value">{}</div>
        </div>
        """.format(checker.iterative_comparisons), unsafe_allow_html=True)
    
    with stat_col2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-label">⏱Waktu Rekursif</div>
            <div class="stat-value">{:.4f}s</div>
        </div>
        """.format(time_rec), unsafe_allow_html=True)
        
        st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Perbandingan Rekursif</div>
            <div class="stat-value">{}</div>
        </div>
        """.format(checker.recursive_comparisons), unsafe_allow_html=True)
        
        st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Kedalaman Rekursi</div>
            <div class="stat-value">{}</div>
        </div>
        """.format(checker.max_recursive_depth), unsafe_allow_html=True)
    
    with stat_col3:
        faster = "Iteratif" if time_iter < time_rec else "Rekursif"
        time_diff_abs = abs(time_iter - time_rec)
        diff_percent = (time_diff_abs / max(time_iter, time_rec)) * 100
        
        st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Lebih Cepat</div>
            <div class="stat-value">{}</div>
        </div>
        """.format(faster), unsafe_allow_html=True)
        
        st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Selisih (Detik)</div>
            <div class="stat-value">{:.6f}s</div>
        </div>
        """.format(time_diff_abs), unsafe_allow_html=True)
        
        st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Selisih (Persen)</div>
            <div class="stat-value">{:.2f}%</div>
        </div>
        """.format(diff_percent), unsafe_allow_html=True)
        
        memory_est = checker.max_recursive_depth * 8
        st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Memory Rekursif</div>
            <div class="stat-value">~s{} bytes</div>
        </div>
        """.format(memory_est), unsafe_allow_html=True)

    
    # Tabel perbandingan
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Tabel Perbandingan Detail</h3>", unsafe_allow_html=True)
    comparison_df = pd.DataFrame({
        'Metrik': [
            'Waktu Eksekusi (detik)',
            'Jumlah Perbandingan',
            'Kompleksitas Waktu',
            'Kompleksitas Ruang',
            'Kedalaman Rekursi',
            'Overhead Memory'
        ],
        'Iteratif': [
            f"{time_iter:.6f}",
            checker.iterative_comparisons,
            'O(n)',
            'O(1)',
            '-',
            'Minimal'
        ],
        'Rekursif': [
            f"{time_rec:.6f}",
            checker.recursive_comparisons,
            'O(n)',
            'O(n)',
            checker.max_recursive_depth,
            f'~{memory_est} bytes'
        ]
    })
    
    st.dataframe(comparison_df, use_container_width=True)

if __name__ == "__main__":
    main()
