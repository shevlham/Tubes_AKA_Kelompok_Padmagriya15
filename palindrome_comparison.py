import time
import sys
from typing import List, Tuple, Dict

class PalindromeChecker:
    def __init__(self):
        self.iterative_comparisons = 0
        self.recursive_comparisons = 0
        self.recursive_depth = 0
        self.max_recursive_depth = 0
        self.visualization_delay = 0.5
        
    def generate_data(self, length: int, order: str = "ascending") -> str:
        """Generate test data based on length and order"""
        if order == "ascending":
            # Generate palindrome ascending
            half = length // 2
            if length % 2 == 0:
                data = ''.join(chr(65 + (i % 26)) for i in range(half))
                return data + data[::-1]
            else:
                data = ''.join(chr(65 + (i % 26)) for i in range(half))
                return data + 'M' + data[::-1]
        else:  # descending
            half = length // 2
            if length % 2 == 0:
                data = ''.join(chr(90 - (i % 26)) for i in range(half))
                return data + data[::-1]
            else:
                data = ''.join(chr(90 - (i % 26)) for i in range(half))
                return data + 'M' + data[::-1]
    
    def print_status(self, algorithm: str, data: str, left: int, right: int, 
                    comparisons: int, is_match: bool = None):
        """Print visualization status"""
        print(f"\n{'='*60}")
        print(f"Algoritma: {algorithm}")
        print(f"Data: {data}")
        print(f"Posisi: Left={left}, Right={right}")
        
        # Visual indicator
        visual = list(' ' * len(data))
        if left < len(data):
            visual[left] = '^'
        if right < len(data) and right != left:
            visual[right] = '^'
        print(f"      {''.join(visual)}")
        
        if is_match is not None:
            status = "MATCH ✓" if is_match else "NOT MATCH ✗"
            print(f"Status: {status}")
        
        print(f"Perbandingan: {comparisons}")
        if algorithm == "REKURSIF":
            print(f"Kedalaman Rekursi: {self.recursive_depth}")
        print(f"{'='*60}")
        
        time.sleep(self.visualization_delay)
    
    def check_palindrome_iterative(self, data: str, visualize: bool = True) -> Tuple[bool, Dict]:
        """Check palindrome using iterative approach"""
        self.iterative_comparisons = 0
        start_time = time.time()
        
        left = 0
        right = len(data) - 1
        
        print(f"\n\n{'#'*60}")
        print(f"MEMULAI ALGORITMA ITERATIF")
        print(f"{'#'*60}")
        
        while left < right:
            self.iterative_comparisons += 1
            
            if visualize:
                is_match = data[left] == data[right]
                self.print_status("ITERATIF", data, left, right, 
                                self.iterative_comparisons, is_match)
            
            if data[left] != data[right]:
                end_time = time.time()
                return False, {
                    'time': end_time - start_time,
                    'comparisons': self.iterative_comparisons,
                    'memory': sys.getsizeof(data),
                    'depth': 0
                }
            
            left += 1
            right -= 1
        
        end_time = time.time()
        return True, {
            'time': end_time - start_time,
            'comparisons': self.iterative_comparisons,
            'memory': sys.getsizeof(data),
            'depth': 0
        }
    
    def check_palindrome_recursive_helper(self, data: str, left: int, right: int, 
                                         visualize: bool = True) -> bool:
        """Recursive helper function"""
        self.recursive_depth += 1
        self.max_recursive_depth = max(self.max_recursive_depth, self.recursive_depth)
        self.recursive_comparisons += 1
        
        if visualize:
            is_match = data[left] == data[right] if left < right else None
            self.print_status("REKURSIF", data, left, right, 
                            self.recursive_comparisons, is_match)
        
        if left >= right:
            self.recursive_depth -= 1
            return True
        
        if data[left] != data[right]:
            self.recursive_depth -= 1
            return False
        
        result = self.check_palindrome_recursive_helper(data, left + 1, right - 1, visualize)
        self.recursive_depth -= 1
        return result
    
    def check_palindrome_recursive(self, data: str, visualize: bool = True) -> Tuple[bool, Dict]:
        """Check palindrome using recursive approach"""
        self.recursive_comparisons = 0
        self.recursive_depth = 0
        self.max_recursive_depth = 0
        
        print(f"\n\n{'#'*60}")
        print(f"MEMULAI ALGORITMA REKURSIF")
        print(f"{'#'*60}")
        
        start_time = time.time()
        result = self.check_palindrome_recursive_helper(data, 0, len(data) - 1, visualize)
        end_time = time.time()
        
        return result, {
            'time': end_time - start_time,
            'comparisons': self.recursive_comparisons,
            'memory': sys.getsizeof(data) * (self.max_recursive_depth + 1),
            'depth': self.max_recursive_depth
        }
    
    def compare_algorithms(self, length: int, order: str = "ascending", 
                          speed: float = 0.5, visualize: bool = True):
        """Compare both algorithms"""
        self.visualization_delay = speed
        
        print(f"\n\n{'*'*60}")
        print(f"PERBANDINGAN EFISIENSI ALGORITMA PALINDROME CHECKING")
        print(f"{'*'*60}")
        print(f"Panjang Data: {length} karakter")
        print(f"Urutan: {order.upper()}")
        print(f"Kecepatan Visualisasi: {speed}s per step")
        print(f"{'*'*60}\n")
        
        # Generate data
        data = self.generate_data(length, order)
        print(f"Data yang dihasilkan: {data}\n")
        
        # Test iterative
        is_palindrome_iter, stats_iter = self.check_palindrome_iterative(data, visualize)
        
        print(f"\n{'='*60}")
        print(f"HASIL ALGORITMA ITERATIF")
        print(f"{'='*60}")
        print(f"Palindrome: {'YA' if is_palindrome_iter else 'TIDAK'}")
        print(f"Waktu Eksekusi: {stats_iter['time']:.6f} detik")
        print(f"Jumlah Perbandingan: {stats_iter['comparisons']}")
        print(f"Penggunaan Memori: {stats_iter['memory']} bytes")
        print(f"{'='*60}\n")
        
        time.sleep(2)
        
        # Test recursive
        is_palindrome_rec, stats_rec = self.check_palindrome_recursive(data, visualize)
        
        print(f"\n{'='*60}")
        print(f"HASIL ALGORITMA REKURSIF")
        print(f"{'='*60}")
        print(f"Palindrome: {'YA' if is_palindrome_rec else 'TIDAK'}")
        print(f"Waktu Eksekusi: {stats_rec['time']:.6f} detik")
        print(f"Jumlah Perbandingan: {stats_rec['comparisons']}")
        print(f"Kedalaman Rekursi Maksimal: {stats_rec['depth']}")
        print(f"Penggunaan Memori: {stats_rec['memory']} bytes")
        print(f"{'='*60}\n")
        
        # Comparison
        print(f"\n{'*'*60}")
        print(f"KESIMPULAN PERBANDINGAN")
        print(f"{'*'*60}")
        
        if stats_iter['time'] < stats_rec['time']:
            print(f"✓ Algoritma ITERATIF lebih cepat")
            print(f"  Selisih: {(stats_rec['time'] - stats_iter['time']):.6f} detik")
        else:
            print(f"✓ Algoritma REKURSIF lebih cepat")
            print(f"  Selisih: {(stats_iter['time'] - stats_rec['time']):.6f} detik")
        
        print(f"\nPerbandingan jumlah operasi: {stats_iter['comparisons']} vs {stats_rec['comparisons']}")
        
        if stats_iter['memory'] < stats_rec['memory']:
            print(f"✓ Algoritma ITERATIF lebih efisien dalam penggunaan memori")
            print(f"  Selisih: {stats_rec['memory'] - stats_iter['memory']} bytes")
        else:
            print(f"✓ Algoritma REKURSIF lebih efisien dalam penggunaan memori")
            print(f"  Selisih: {stats_iter['memory'] - stats_rec['memory']} bytes")
        
        print(f"\nKedalaman rekursi maksimal: {stats_rec['depth']}")
        print(f"{'*'*60}\n")

def main():
    print("=" * 60)
    print("PROGRAM PERBANDINGAN ALGORITMA PALINDROME")
    print("=" * 60)
    
    checker = PalindromeChecker()
    
    # Get user input
    try:
        length = int(input("\nMasukkan panjang data (3-1000): "))
        if length < 3 or length > 1000:
            print("Panjang data harus antara 3 dan 1000!")
            return
        
        print("\nPilih urutan data:")
        print("1. Ascending")
        print("2. Descending")
        order_choice = input("Pilihan (1/2): ")
        order = "ascending" if order_choice == "1" else "descending"
        
        speed = float(input("\nMasukkan kecepatan visualisasi (0.1-2.0 detik): "))
        if speed < 0.1 or speed > 2.0:
            speed = 0.5
        
        visualize = input("\nTampilkan visualisasi step-by-step? (y/n): ").lower() == 'y'
        
        # Run comparison
        checker.compare_algorithms(length, order, speed, visualize)
        
    except ValueError:
        print("Input tidak valid!")
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh user.")

if __name__ == "__main__":
    main()
