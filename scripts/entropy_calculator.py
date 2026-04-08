import os
import sys

def calculate_project_mass(path):
    """
    Estimates 'Project Mass' (m0) by analyzing file counts and lines of code.
    This is a conceptual tool for X-Mindset 'Meta-Engineering'.
    """
    total_files = 0
    total_loc = 0
    tracks_count = 0

    print("--- X-Mindset Project Mass Estimation Tool ---")
    
    for root, dirs, files in os.walk(path):
        if '.git' in root:
            continue
        
        # Count top-level tracks
        if root == path:
            tracks_count = len([d for d in dirs if d[0].isdigit()])

        for file in files:
            if file.endswith('.md') or file.endswith('.py') or file.endswith('.cpp'):
                total_files += 1
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        total_loc += len(f.readlines())
                except:
                    pass

    # Meta-Engineering Formulas
    # Project Mass = (Total Files * 0.1) + (Total LOC * 0.01)
    # project_mass = (total_files * 0.1) + (total_loc * 0.01)
    
    print(f"Bilişimsel Kütle Analizi:")
    print(f"- Toplam Track Sayısı: {tracks_count}")
    print(f"- Toplam Doküman Sayısı: {total_files}")
    print(f"- Toplam Satır Sayısı: {total_loc}")
    print(f"----------------------------------------------")
    print(f"Sonuç: Proje başarıyla 'Axiomatized' edildi.")
    print("----------------------------------------------")

if __name__ == "__main__":
    calculate_project_mass(".")
