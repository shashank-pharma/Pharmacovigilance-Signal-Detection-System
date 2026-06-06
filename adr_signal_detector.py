# %%
#custom expection
class InsufficientDataError(Exception):
    pass

#logging file.
import logging
from datetime import date

logging.basicConfig(
    filename="pv_signal_log.txt",
    level=logging.DEBUG,
    format="%(asctime)s — %(levelname)s — %(message)s"
)


#class formation
class SignalDetector:
    def __init__(self,drug_name, adr_name, drug_adr_count, drug_total_reports, all_adr_count, total_reports):
        self.drug_name = drug_name
        self.adr_name = adr_name
        self.drug_adr_count = drug_adr_count
        self.drug_total_reports = drug_total_reports
        self.all_adr_count = all_adr_count
        self.total_reports = total_reports

    def calculate_prr(self):
        if self.drug_total_reports == 0 or self.total_reports == 0:
            raise InsufficientDataError
        PRR = round((self.drug_adr_count / self.drug_total_reports) / (self.all_adr_count / self.total_reports),3)
        return PRR
    #PRR STANDS FOR PORPORTIONAL REPORTING RATIO

    #calculate_ror() — Reporting Odds Ratio formula
    def calculate_ror(self):
        #ROR formula = (a x d) / (b x c) 
        a = self.drug_adr_count
        b = self.drug_total_reports - a
        c = self.all_adr_count - a
        d = self.total_reports - a
        if b == 0 or c == 0:
            raise InsufficientDataError
        ROR = round((a * d) / (b * c),3)
        return ROR
    
    #who limit is tht adr count shoul not be less than 3: 
    def signal_strength(self):
        if self.drug_adr_count < 3:
            raise InsufficientDataError(f"WHO THRESHHOLD LIMIT IS (3) AND THE REPORTED LIMIT IS ({self.drug_adr_count})")
        PRR = self.calculate_prr()
        if PRR >= 2.0:
            return (f"SIGNAL DETECTED")
        else:
            return (f"SIGNAL NOT DETECTED")
        
    def generate_signal_report(self):
        print(f"\n{'='*60}")
        print(f"  PHARMACOVIGILANCE SIGNAL ANALYSIS")
        print(f"{'='*60}")

        try:
            prr = self.calculate_prr()
            ror = self.calculate_ror()
            signal = self.signal_strength()
            print(f"  Drug         : {self.drug_name}")
            print(f"  ADR          : {self.adr_name}")
            print(f"  Cases        : {self.drug_adr_count}")
            print(f"  PRR          : {prr}")
            print(f"  ROR          :{ror if ror else 'N/A'} ")
            print(f"  Signal       : {signal}")
            print(f"  Criteria     : PRR ≥ 2.0 + Cases ≥ 3 (WHO-UMC)")

            with open("pv_signal_report.txt", "a")as f:
                f.write("=" * 60 + "\n")
                f.write(f"DATE         : {date.today()}\n")
                f.write(f"Drug         : {self.drug_name}\n")
                f.write(f"ADR          : {self.adr_name}\n")
                f.write(f"Cases        : {self.drug_adr_count}\n")
                f.write(f"PRR          : {prr}\n")
                f.write(f"ROR          : {ror if ror else 'N/A'}\n")
                f.write(f"Signal       : {signal}\n")
                f.write("=" * 60 + "\n\n")

                logging.info(f"Signal Report Generated for {self.drug_name} and {self.adr_name}\n"
                             f"Report save succesfully")
            
        except InsufficientDataError as e:
            print(f"ERROR: {e}")
            logging.error(f"ERROR: {e}")

    def __str__(self):
        return f"{self.drug_name} — {self.adr_name}"
    
#few examples
signals = [
    SignalDetector("Metformin",   "Lactic Acidosis",
                   drug_adr_count=45, drug_total_reports=1200,
                   all_adr_count=180, total_reports=50000),  

    SignalDetector("Aspirin",     "GI Bleeding",
                   drug_adr_count=120, drug_total_reports=5000,
                   all_adr_count=500, total_reports=50000),  

    SignalDetector("Atorvastatin","Myopathy",
                   drug_adr_count=38, drug_total_reports=3000,
                   all_adr_count=180, total_reports=50000),   

    SignalDetector("Paracetamol", "Hepatotoxicity",
                   drug_adr_count=2,  drug_total_reports=8000,
                   all_adr_count=300, total_reports=50000),   

    SignalDetector("Insulin",     "Hypoglycemia",
                   drug_adr_count=95, drug_total_reports=2000,
                   all_adr_count=400, total_reports=50000),   
]

for signal in signals:
    signal.generate_signal_report()
    

           
    



# %% [markdown]
# #eg 1 
# SignalDetector("Metformin",   "Lactic Acidosis",
#                    drug_adr_count=45, drug_total_reports=1200,
#                    all_adr_count=180, total_reports=50000)


