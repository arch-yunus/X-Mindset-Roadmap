import os
import sys
import math
from datetime import datetime

class XMindsetAnalyzer:
    """
    X-Mindset 'Meta-Engineering' Analiz Aracı v2.0
    Projenin 'Bilişimsel Kütle' (m0) ve 'Aksiyom Yoğunluğu' değerlerini hesaplar.
    """
    
    def __init__(self, target_path="."):
        self.target_path = target_path
        self.stats = {
            'total_files': 0,
            'total_loc': 0,
            'md_files': 0,
            'md_loc': 0,
            'code_files': 0,
            'code_loc': 0,
            'tracks': []
        }
        self.axioms_found = 0

    def analyze(self):
        for root, dirs, files in os.walk(self.target_path):
            if any(exclude in root for exclude in ['.git', '__pycache__', 'assets']):
                continue
            
            # Identify tracks
            if root == self.target_path:
                self.stats['tracks'] = [d for d in dirs if d[0].isdigit()]

            for file in files:
                file_path = os.path.join(root, file)
                ext = os.path.splitext(file)[1].lower()
                
                if ext in ['.md', '.py', '.cpp', '.hpp', '.rs']:
                    self.stats['total_files'] += 1
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            lines = f.readlines()
                            line_count = len(lines)
                            self.stats['total_loc'] += line_count
                            
                            if ext == '.md':
                                self.stats['md_files'] += 1
                                self.stats['md_loc'] += line_count
                                # Count axioms (lines starting with '>')
                                self.axioms_found += sum(1 for line in lines if line.strip().startswith('>'))
                            else:
                                self.stats['code_files'] += 1
                                self.stats['code_loc'] += line_count
                    except:
                        pass

    def calculate_metrics(self):
        # Tsiolkovsky-based Mass Calculation
        # m0 = (File Count * 1.5) + (LOC * 0.1)
        mass = (self.stats['total_files'] * 1.5) + (self.stats['total_loc'] * 0.1)
        
        # Axiom Density (Axioms per 100 lines of MD)
        density = (self.axioms_found / max(1, self.stats['md_loc'])) * 100
        
        # Velocity Score (Conceptual)
        velocity = 100 / (1 + math.log(mass + 1))
        
        return mass, density, velocity

    def report(self):
        mass, density, velocity = self.calculate_metrics()
        
        print("\n" + "="*50)
        print("🚀 X-MINDSET PROJECT ANALYZER v2.0")
        print("="*50)
        print(f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-"*50)
        print(f"📊 Genel İstatistikler:")
        print(f"  - Toplam Track Sayısı   : {len(self.stats['tracks'])}")
        print(f"  - Toplam Dosya          : {self.stats['total_files']} (MD: {self.stats['md_files']}, Code: {self.stats['code_files']})")
        print(f"  - Toplam Satır (LOC)    : {self.stats['total_loc']}")
        print("-"*50)
        print(f"⚛️ Meta-Engineering Metrikleri:")
        print(f"  - Proje Kütlesi (m0)    : {mass:.2f} units")
        print(f"  - Aksiyom Yoğunluğu     : {density:.2f}%")
        print(f"  - Teorik Hız (Delta-v)  : {velocity:.2f}%")
        print("-"*50)
        
        if density < 2.0:
            print("⚠️ UYARI: Düşük Aksiyom Yoğunluğu. Dogmaları temizleyin.")
        elif mass > 500:
            print("⚠️ UYARI: Yüksek Kütle (Bloat). Step 2 (SİL) uygulayın.")
        else:
            print("✅ SİSTEM OPTİMAL: Yüksek hız ve düşük kütle tespiti.")
        
        print("="*50 + "\n")

if __name__ == "__main__":
    analyzer = XMindsetAnalyzer()
    analyzer.analyze()
    analyzer.report()
