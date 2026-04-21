import streamlit as st
import json

# ── 페이지 설정 ──────────────────────────────────────────────
st.set_page_config(
    page_title="ED Quick Reference",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── 데이터 ───────────────────────────────────────────────────
DATA = [
  {
  "Chief Complaint": "Fever (Adult) / 발열",
  "Initial Action": "1. Assess ABCs \n2. qSOFA: GCS<15, RR≥22, SBP≤100 \n3. Fluid resuscitation for sepsis or shock.",
  "Red Flag Signs & Must-not-miss": "1. Septic Shock \n2. Meningitis/Encephalitis \n3. Neutropenic fever (chemotherapy) \n4. Infective Endocarditis (New heart murmur).\n5. Necrotizing Fasciitis (Pain out of proportion to skin findings).",
  "Common Causes (Top 5)": "1. Upper Respiratory Infection (URI).\n2. Urinary Tract Infection (UTI).\n3. Pneumonia.\n4. Cellulitis/Skin and Soft Tissue Infection (SSTI).\n5. Gastroenteritis.",
  "Key History": "1. Duration and pattern of fever.\n2. Associated symptoms .\n3. Recent surgery or invasive procedures.\n4. Travel history and medication use (Drug fever).\n5. Immunocompromised status (DM, HIV, Cancer).",
  "Physical Exam": "1. General appearance \n2. Skin exam (Rashes, petechiae, surgical sites).\n3. Auscultation (Lung crackles, heart murmurs).\n4. Neurological exam (Meningeal signs).",
  "Tests & Purpose": "1. CBC/CRP/Procalcitonin: Inflammation \n2. Lactate : r/o hypoxia \n3. Blood & Urine Cultures \n4. UA/UC: r/o UTI \n5. CXR : r/o pneumonia \n6. CSF Analysis: r/o meningitis",
  "Management": "1. Antipyretics : AAP or NSAIDs \n2. Early empirical broad-spectrum Abx for suspected sepsis \n3. Fluid resuscitation",
  "Consult & Disposition": "1. Admit for sepsis, high-risk infections, or failure of outpatient treatment.\n2. Consult Infectious Disease or Surgery as indicated.",
  "Discharge & Warning": "1. Discharge if vitals are stable, source is identified/benign, and PO intake is possible.\n2. Warning: Return - mental change, dyspnea, persistent high fever",
  "Pearls & Pitfalls": "1. Elderly patients may not manifest fever even with severe infection (occult sepsis).\n2. Always check for indwelling devices (IV lines, catheters) as potential sources.",
},
    {
        "Chief Complaint": "Fever (Pediatric)",
        "Initial Action": "1. Pediatric Assessment Triangle (PAT) for severity.\n2. Maintain airway and provide O2 if needed.\n3. Correct dehydration (IV or PO rehydration).",
        "Red Flag Signs & Must-not-miss": "1. Neonatal Fever (<28 days old: assume Serious Bacterial Infection).\n2. Bulging fontanelle or lethargy (Meningitis).\n3. Petechial/Purpuric rash (Meningococcemia).\n4. Inconsolable crying or decreased activity.",
        "Common Causes (Top 5)": "1. Viral URI.\n2. Otitis Media.\n3. Urinary Tract Infection (Common 'occult' source in peds).\n4. Gastroenteritis.\n5. Bronchiolitis/Pneumonia.",
        "Key History": "1. Precise temperature and measurement method.\n2. Activity level and hydration status (Wet diapers).\n3. Immunization status.\n4. Exposure to ill contacts.",
        "Physical Exam": "1. Check ears (Otoscopy) and throat.\n2. Skin exam for rashes.\n3. Bulging/depressed fontanelle.\n4. Lung auscultation and abdominal palpation.",
        "Tests & Purpose": "1. <28 days: Full septic workup (CBC, UA/UC, BC, CSF analysis).\n2. 29-90 days: Follow Rochester/Philadelphia criteria.\n3. UA/UC: Essential for FUO (Fever of Unknown Origin).",
        "Management": "1. Antipyretics: Acetaminophen (15mg/kg) or Ibuprofen (10mg/kg).\n2. Age-appropriate antibiotics for suspected SBI.\n3. Rehydration.",
        "Consult & Disposition": "1. Admit all neonates (<28 days) with fever.\n2. Admit for toxic appearance or inability to tolerate PO.",
        "Discharge & Warning": "1. Discharge if stable and viral etiology likely.\n2. Warning: Return if seizures, lethargy, or poor feeding occur.",
        "Pearls & Pitfalls": "1. Response to antipyretics does NOT rule out serious bacterial infection.\n2. A negative physical exam in a febrile child often necessitates a UA/UC.",
    },
    {
        "Chief Complaint": "General Weakness/Malaise",
        "Initial Action": "1. Check Vitals (Focus on BP and HR).\n2. Bedside Glucose (BST).\n3. Cardiac monitoring and EKG.",
        "Red Flag Signs & Must-not-miss": "1. Atypical MI (Especially in elderly/women).\n2. Sepsis (Early stage).\n3. Severe Electrolyte Imbalance (e.g., Hyperkalemia).\n4. Acute Anemia/GI Bleed.\n5. Adrenal Insufficiency.",
        "Common Causes (Top 5)": "1. Viral/Bacterial Infection.\n2. Medication side effects (Beta-blockers, Sedatives).\n3. Dehydration/Electrolyte imbalance (Hyponatremia).\n4. Anemia.\n5. Depression/Psychosocial factors.",
        "Key History": "1. Define 'weakness' (True motor weakness vs. fatigue).\n2. Onset and duration.\n3. Recent medication changes.\n4. Associated symptoms (Chest pain, melena, dizziness).",
        "Physical Exam": "1. Neurological exam (Focal deficits).\n2. Conjunctival pallor (Anemia).\n3. Rectal exam (DRE) if GI bleed suspected.\n4. Orthostatic vitals.",
        "Tests & Purpose": "1. CBC/Electrolytes/BUN/Cr: Check for anemia, metabolic issues.\n2. EKG: Rule out arrhythmias or ischemia.\n3. Cardiac markers: For atypical ACS.",
        "Management": "1. IV fluids for dehydration.\n2. Correct electrolyte abnormalities.\n3. Supportive care based on etiology.",
        "Consult & Disposition": "1. Admit for unstable vitals or serious underlying cause (MI, severe anemia).\n2. Consider observation for elderly with failure to thrive.",
        "Discharge & Warning": "1. Discharge if workup is negative and patient is hemodynamically stable.\n2. Warning: Return if syncopal episodes, chest pain, or worsening symptoms occur.",
        "Pearls & Pitfalls": "1. 'Weakness' in the elderly is a high-risk complaint; don't dismiss it as 'just aging' without a thorough workup.",
    },
    {
        "Chief Complaint": "Altered Mental Status / 멘체",
        "Initial Action": "1. ABCs (Consider intubation if GCS < 8).\n2. Bedside Glucose (BST) - Rule out hypoglycemia immediately.\n3. Consider Naloxone for suspected opioid overdose.",
        "Red Flag Signs & Must-not-miss": "1. Intracranial Hemorrhage/Stroke.\n2. CNS Infection (Meningitis/Encephalitis).\n3. Non-convulsive Status Epilepticus.\n4. Hypertensive Encephalopathy.\n5. Wernicke's Encephalopathy.",
        "Common Causes (Top 5)": "1. Metabolic Encephalopathy (Hypoglycemia, Na+/Ca2+ imbalance).\n2. Infection (Sepsis, UTI in elderly).\n3. Toxin/Drug Ingestion (Alcohol, Sedatives).\n4. Stroke/TIA.\n5. Trauma (SDH/EDH).",
        "Key History": "1. Baseline mental status (Time of 'Last Known Normal').\n2. Speed of onset.\n3. History of DM, Liver Cirrhosis, or Renal Failure.\n4. Potential for toxin exposure.",
        "Physical Exam": "1. GCS score and Pupillary response.\n2. Focal neurological deficits (Hemiparesis).\n3. Signs of trauma or meningismus.",
        "Tests & Purpose": "1. Non-contrast Brain CT: Rule out structural lesions.\n2. ABGA/VBG, Ammonia, Electrolytes: Metabolic causes.\n3. UA/UC and Cultures: Infectious source.\n4. LP: If CNS infection is suspected.",
        "Management": "1. Secure airway and oxygenation.\n2. Targeted treatment (D50W for hypoglycemia, Antidotes, Antibiotics).\n3. Manage increased ICP if suspected.",
        "Consult & Disposition": "1. Consult Neurology/Neurosurgery for structural/neurologic causes.\n2. Admission is usually required for workup and management.",
        "Discharge & Warning": "1. Rarely discharged unless a simple, reversible cause (e.g., hypoglycemia) is fully resolved and stable.\n2. Warning: Close observation by a caregiver is mandatory.",
        "Pearls & Pitfalls": "1. Use the 'AEIOU-TIPS' mnemonic to ensure a comprehensive differential diagnosis.\n2. Always check for 'occult' infection in elderly patients with AMS.",
    },
    {
        "Chief Complaint": "Syncope / 실신",
        "Initial Action": "1. Assess ABCs and EKG monitoring.\n2. Bedside Glucose (BST).\n3. IV access and fluid bolus for hypotension.",
        "Red Flag Signs & Must-not-miss": "1. Cardiac Syncope (Arrhythmias, Structural heart disease).\n2. Massive Pulmonary Embolism.\n3. Aortic Dissection.\n4. Ruptured Ectopic Pregnancy/AAA.\n5. Subarachnoid Hemorrhage.",
        "Common Causes (Top 5)": "1. Vasovagal Syncope (Neurocardiogenic).\n2. Orthostatic Hypotension.\n3. Cardiac Arrhythmia.\n4. Situational Syncope (Micturition, Coughing).\n5. Medication-induced.",
        "Key History": "1. Prodromal symptoms (Nausea, sweating vs. sudden onset).\n2. Position when occurred (Supine syncope is high risk).\n3. Relation to exertion.\n4. Family history of sudden cardiac death.",
        "Physical Exam": "1. Orthostatic vitals.\n2. Heart auscultation (Murmurs of AS or HCM).\n3. Neurological exam.\n4. DRE (Check for GI bleed).",
        "Tests & Purpose": "1. 12-lead EKG: Essential to rule out Brugada, WPW, Long QT, heart block.\n2. CBC/Electrolytes: Anemia/metabolic issues.\n3. Pregnancy test (hCG): For women of childbearing age.\n4. POCUS: Check for AAA or cardiac contractility.",
        "Management": "1. Treat underlying cause.\n2. Fluid resuscitation for orthostasis.\n3. Cardiac monitoring for suspected arrhythmias.",
        "Consult & Disposition": "1. Use risk scores (e.g., San Francisco Syncope Rule).\n2. Admit for high-risk features (History of CHF, abnormal EKG, severe anemia).",
        "Discharge & Warning": "1. Discharge if low-risk (classic vasovagal) with primary care follow-up.\n2. Warning: No driving until cleared, return if recurrence or chest pain occurs.",
        "Pearls & Pitfalls": "1. A normal EKG does not rule out all cardiac causes but is the most important initial test.\n2. Syncope while supine or during exercise is a major red flag for cardiac origin.",
    },
    {
    "Chief Complaint": "Shock / Hypotension ",
    "Initial Action": "1. Secure large-bore IV access (x2) and provide supplemental O2.\n2. Initiate RUSH exam (Rapid Ultrasound in Shock) to differentiate etiology.\n3. Fluid challenge (30mL/kg crystalloid) if no signs of volume overload.\n4. Prepare vasopressors (Norepinephrine as first-line for most)." ,
    "Red Flag Signs & Must-not-miss": "1. Obstructive Shock: Tension pneumothorax, Cardiac tamponade, Massive PE.\n2. Cardiogenic Shock: Acute MI, Acute valvular rupture.\n3. Distributive Shock: Anaphylaxis, Sepsis.\n4. Hypovolemic Shock: Ruptured AAA, Massive GI bleed.\n5. Adrenal Crisis: Refractory hypotension (consider Hydrocortisone).",
    "Common Causes (Top 5)": "1. Sepsis (Distributive).\n2. Dehydration / Hemorrhage (Hypovolemic).\n3. Heart Failure / MI (Cardiogenic).\n4. Medication side effects (Antihypertensives).\n5. Anaphylaxis.",
    "Key History": "1. Presence of fever or recent infection.\n2. History of trauma, chest pain, or abdominal pain.\n3. Melena or hematemesis.\n4. Recent medication changes or known allergies.\n5. Symptoms of 'occult' bleeding (e.g., lightheadedness, syncope).",
    "Physical Exam": "1. Skin perfusion: Warm (distributive) vs. Cold (cardiogenic/hypovolemic).\n2. Jugular Venous Distension (JVD): Present in cardiogenic/obstructive shock.\n3. Lung auscultation: Crackles (HF) vs. Clear (sepsis/hypovolemia).\n4. Abdominal tenderness or pulsatile mass.",
    "Tests & Purpose": "1. Serum Lactate: Marker of tissue hypoperfusion and prognosis.\n2. CBC, Electrolytes, Renal/Liver function: Assess end-organ damage.\n3. EKG: Rule out MI or arrhythmia-induced shock.\n4. Type & Cross: If hemorrhage is suspected.",
    "Management": "1. Aggressive fluid resuscitation (balanced crystalloids preferred).\n2. Early antibiotics for suspected sepsis (within 1 hour).\n3. Source control (surgery, IR) for hemorrhage.\n4. Inotropes (Dobutamine) for cardiogenic shock.",
    "Consult & Disposition": "1. Admission to ICU is mandatory for most shock states.\n2. Consult Cardiology (MI), Surgery (Bleed), or ID (Sepsis) as needed.",
    "Discharge & Warning": "1. Do not discharge if hypotensive or if cause is not fully reversed.\n2. Warning: High risk of rapid deterioration; close monitoring required.",
    "Pearls & Pitfalls": "1. Remember: Blood pressure can be normal in early shock due to compensatory mechanisms (Look at Lactate).\n2. Avoid over-resuscitation in patients with cardiogenic shock/CHF."
  },
  {
    "Chief Complaint": "Dizziness / Vertigo / 어지럼증",
    "Initial Action": "1. v/s & neurological status.\n2. BST check .\n3. IV fluids & antiemetics",
    "Red Flag Signs & Must-not-miss": "1. Posterior Circulation Stroke (Cerebellar/Brainstem) \n2. Vertebrobasilar Insufficiency (VBI) \n3. Vertebral Artery Dissection (Neck pain + vertigo) \n4. Cardiac Arrhythmia (Syncope/palpitations) \n5. Orthostatic Hypotension.",
    "Common Causes (Top 5)": "1. Benign Paroxysmal Positional Vertigo (BPPV) \n2. Vestibular Neuritis / Labyrinthitis \n3. Meniere’s Disease \n4. Vestibular Migraine.\n5. Orthostatic Hypotension / Medication-induced.",
    "Key History": "1. Duration: Seconds (BPPV) vs. Hours/Days (Neuritis/Stroke) \n2. Triggers: Head movement, standing up, or spontaneous \n3. Associated Sx: Hearing loss, tinnitus, focal neuro deficits (diplopia, dysarthria).",
    "Physical Exam": "1. HINTS Exam (Head Impulse, Nystagmus, Test of Skew): Only in continuous vertigo. VN vs central \n2. Dix-Hallpike : r/o BPPV \n3. Gait : Truncal ataxia suggests central origin.",
    "Tests & Purpose": "1. Brain MRI (DWI): Gold standard for posterior stroke \n2. EKG: r/o arrhythmia-related dizziness \n3. Orthostatic Vitals ",
    "Management": "1. Epley maneuver (for posterior canal BPPV).\n2. Vestibular suppressants (Meclizine, Diazepam) - limit to 48-72 hours \n3. Antiemetics (Metoclopramide, Lorazepam)",
    "Consult & Disposition": "1. Neurology consult for suspected central vertigo or HINTS positive for stroke.\n2. Discharge peripheral vertigo if symptoms are controlled and patient can walk.",
    "Discharge & Warning": "1. Discharge with vestibular exercises and follow-up.\n2. Warning: Return immediately if new neurological deficits, severe headache, or inability to walk occur.",
    "Pearls & Pitfalls": "1. 'Infantile' HINTS (HINTS+) is more sensitive for stroke than early MRI.\n2. Do not use the HINTS exam in patients with episodic (non-continuous) vertigo."
  },
  {
    "Chief Complaint": "Allergic Reaction / Anaphylaxis",
    "Initial Action": "1. Assess Airway/Breathing; look for stridor or wheezing.\n2. Anaphylaxis? **Epinephrine (1:1000) 0.3-0.5mg IM** immediately.\n3. Supplemental O2 and high-flow IV fluids for hypotension.",
    "Red Flag Signs & Must-not-miss": "1. Upper airway obstruction (Laryngeal edema).\n2. Hypotension / Cardiovascular collapse.\n3. Biphasic reaction (Return of symptoms after 4-12 hours).\n4. Beta-blocker use (May require Glucagon for refractory shock).",
    "Common Causes (Top 5)": "1. Foods (Nuts, Shellfish).\n2. Medications (Antibiotics, NSAIDs, Contrast).\n3. Insect Stings (Bees, Wasps).\n4. Latex.\n5. Idiopathic.",
    "Key History": "1. Exposure to known/suspected allergens.\n2. Timing of onset (Symptoms within minutes/hours).\n3. Prior history of severe reactions.\n4. History of asthma (Increases risk of severe anaphylaxis).",
    "Physical Exam": "1. Skin: Urticaria (hives), angioedema (swelling of lips/tongue/eyelids).\n2. Respiratory: Wheezing, stridor, accessory muscle use.\n3. Cardiovascular: Tachycardia, hypotension.",
    "Tests & Purpose": "1. Clinical diagnosis: Do not wait for labs.\n2. EKG monitoring: For arrhythmia or ischemia in older adults.\n3. Serum Tryptase (Optional, for post-event confirmation).",
    "Management": "1. Epinephrine IM (The primary life-saving treatment).\n2. Adjuncts: H1 blockers (Diphenhydramine), H2 blockers (Famotidine), Steroids (Methylprednisolone).\n3. Inhaled Beta-agonists (Albuterol) for wheezing.",
    "Consult & Disposition": "1. Observe anaphylaxis for at least 4-8 hours (up to 24h) for biphasic reactions.\n2. Admit for airway involvement, persistent hypotension, or high-risk features.",
    "Discharge & Warning": "1. Prescribe Epinephrine auto-injector (EpiPen) and provide training.\n2. Warning: Return immediately if rash recurs, breathing becomes difficult, or swelling returns.",
    "Pearls & Pitfalls": "1. Under-dosing Epinephrine is the most common mistake in EM.\n2. Steroids and antihistamines do NOT treat the life-threatening features of anaphylaxis; only Epi does."
  },
  {
    "Chief Complaint": "Poisoning / Overdose / DI",
    "Initial Action": "1. Assess ABCs and secure airway (especially if GCS < 8).\n2. Check Bedside Glucose (BST).\n3. Continuous EKG monitoring (Check QRS/QTc intervals).\n4. Contact Poison Control Center.",
    "Red Flag Signs & Must-not-miss": "1. Tricyclic Antidepressants (TCA): QRS widening, seizures, arrhythmias.\n2. Calcium Channel Blockers (CCB) / Beta-blockers: Refractory shock.\n3. Acetaminophen: Delayed liver failure (Silent early phase).\n4. Carbon Monoxide: Altered mental status.\n5. Organophosphates: Cholinergic crisis (SLUDGE).",
    "Common Causes (Top 5)": "1. Acetaminophen (Tylenol).\n2. Benzodiazepines / Opioids.\n3. Psychotropic meds (SSRIs, TCAs, Lithium).\n4. Ethanol / Toxic alcohols (Methanol, Ethylene Glycol).\n5. Household chemicals / Carbon Monoxide.",
    "Key History": "1. Substance(s), Dose, and Time of ingestion.\n2. Intent (Suicidal vs. Accidental).\n3. Co-ingestants (especially Alcohol).\n4. Bring the pill bottles if possible.",
    "Physical Exam": "1. Toxidromes: Check pupils, skin moisture, bowel sounds, mental status.\n2. Temperature: Hyperthermia (Serotonin syndrome, Sympathomimetics).\n3. Trauma: Look for head injury or pressure sores.",
    "Tests & Purpose": "1. Acetaminophen and Salicylate levels: Essential screening for all intentional ODs.\n2. EKG: To screen for cardiotoxicity.\n3. Osmolar & Anion Gap: For toxic alcohol ingestion.",
    "Management": "1. Activated Charcoal (if within 1 hour and airway secure).\n2. Specific Antidotes: NAC (Acetaminophen), Narcan (Opioids), Flumazenil (Benzos - use with caution), Digifab (Digoxin).\n3. Whole Bowel Irrigation (for body packers or SR meds).",
    "Consult & Disposition": "1. Psychiatry consult for all intentional self-harm.\n2. ICU admission for high-toxicity substances or unstable vitals.",
    "Discharge & Warning": "1. Discharge after appropriate observation (usually 6-12h) if asymptomatic and non-toxic levels.\n2. Warning: Psychiatry clearance is required before discharge for suicidal patients.",
    "Pearls & Pitfalls": "1. Don't trust the patient's history of 'what' they took; treat the Toxidrome.\n2. 'One pill can kill' - be wary of CCB or TCA ingestion in children."
  },
  {
    "Chief Complaint": "Just not feeling well (Malaise)",
    "Initial Action": "1. Thorough vitals check (Search for subtle abnormalities).\n2. Bedside Glucose (BST).\n3. Screen for frailty and functional decline in elderly.",
    "Red Flag Signs & Must-not-miss": "1. Atypical Sepsis (Especially in elderly without fever).\n2. Silent MI.\n3. Electrolyte Imbalance (e.g., Hyponatremia).\n4. Occult malignancy.\n5. Subacute Adrenal Insufficiency.",
    "Common Causes (Top 5)": "1. Occult Infection (UTI, Pneumonia).\n2. Dehydration / Malnutrition.\n3. Medication side effects or interactions.\n4. Anemia.\n5. Depression / Anxiety.",
    "Key History": "1. Change in Activities of Daily Living (ADL).\n2. Recent medication changes or polypharmacy.\n3. Weight loss or night sweats.\n4. Social isolation or lack of support.",
    "Physical Exam": "1. Look for subtle infection: Pressure ulcers, joint swelling, dental issues.\n2. Volume status: Mucous membranes, skin turgor.\n3. Basic cognitive screen.",
    "Tests & Purpose": "1. CBC, UA, Electrolytes, BUN/Cr: Basic metabolic/infectious screen.\n2. EKG: To rule out 'painless' ischemia.\n3. Chest X-ray: Check for occult pneumonia or failure.",
    "Management": "1. Rehydration and nutritional support if needed.\n2. Optimize medications (Stop unnecessary/risky drugs).\n3. Address the specific underlying cause identified.",
    "Consult & Disposition": "1. Admission for elderly patients with 'failure to thrive' and no support system.\n2. Internal Medicine or Geriatrics follow-up.",
    "Discharge & Warning": "1. Discharge if vitals/labs are normal and ADL is manageable.\n2. Warning: Return if fever, confusion, or inability to perform basic tasks occurs.",
    "Pearls & Pitfalls": "1. In an elderly patient, 'vague malaise' is a diagnosis of exclusion; assume a serious underlying cause until proven otherwise."
  },
  {
    "Chief Complaint": "Chest Pain / 흉통",
    "Initial Action": "1. 12-lead EKG within 10 minutes of arrival.\n2. Oxygen if SpO2 < 94%, IV access, and cardiac monitoring.\n3. Administer Aspirin (162–325 mg, chewed) unless contraindicated.",
    "Red Flag Signs & Must-not-miss": "1. Acute Coronary Syndrome (ACS).\n2. Aortic Dissection (Sudden, tearing pain to back).\n3. Pulmonary Embolism (PE).\n4. Tension Pneumothorax.\n5. Esophageal Rupture (Boerhaave syndrome).",
    "Common Causes (Top 5)": "1. Musculoskeletal / Chest wall pain.\n2. Gastroesophageal Reflux Disease (GERD).\n3. Stable/Unstable Angina.\n4. Anxiety / Panic Disorder.\n5. Pneumonia / Pleurisy.",
    "Key History": "1. Quality (Pressure, tearing, sharp) and radiation (Jaw, left arm, back).\n2. Risk factors (HTN, DM, Smoking, Family history, Cocaine use).\n3. Onset (Sudden vs. Gradual) and duration.\n4. Provocative/Palliative factors (Exertion, NTG response).",
    "Physical Exam": "1. Comparison of BP in both arms (Dissection).\n2. Heart sounds (New murmurs, S3/S4).\n3. Lung auscultation (Breath sounds, crackles).\n4. Chest wall palpation (Tenderness).",
    "Tests & Purpose": "1. Serial Troponin: Identify myocardial injury.\n2. Chest X-ray: Check for widened mediastinum, pneumothorax, or pneumonia.\n3. D-dimer: Rule out PE (in low-risk patients via PERC/Wells).\n4. CT Angiography: For suspected dissection or PE.",
    "Management": "1. ACS: Heparin, Nitroglycerin, Beta-blockers (if indicated).\n2. Dissection: HR and BP control (Esmolol/Nicardipine).\n3. PE: Anticoagulation or Thrombolytics.",
    "Consult & Disposition": "1. Cardiology: STEMI/NSTEMI for PCI or admission.\n2. Cardiothoracic Surgery: Aortic dissection.\n3. Use HEART score for low-risk chest pain disposition.",
    "Discharge & Warning": "1. Discharge only if life-threatening causes are ruled out and HEART score is low.\n2. Warning: Return immediately for worsening pain, SOB, or diaphoresis.",
    "Pearls & Pitfalls": "1. A normal initial EKG does not rule out ACS; serial EKGs are mandatory if pain persists.\n2. Beware of 'painless' MI in elderly, diabetic, or female patients."
  },
  {
    "Chief Complaint": "Dyspnea / Shortness of Breath / 호흡곤란",
    "Initial Action": "1. Assess airway and provide supplemental O2 (target SpO2 > 92%).\n2. Continuous cardiac monitoring and capnography.\n3. Bedside Ultrasound (POCUS/BLUE protocol) for rapid assessment.",
    "Red Flag Signs & Must-not-miss": "1. Upper Airway Obstruction (Epiglottitis, foreign body).\n2. Tension Pneumothorax.\n3. Acute Pulmonary Edema / Heart Failure.\n4. Status Asthmaticus / Severe COPD exacerbation.\n5. Pulmonary Embolism.",
    "Common Causes (Top 5)": "1. Asthma / COPD exacerbation.\n2. Acute Decompensated Heart Failure (ADHF).\n3. Pneumonia.\n4. Pulmonary Embolism.\n5. Anxiety / Hyperventilation Syndrome.",
    "Key History": "1. Speed of onset (Sudden suggests PE or Pneumothorax).\n2. Orthopnea or Paroxysmal Nocturnal Dyspnea (PND) (Heart failure).\n3. History of Asthma, COPD, or CHF.\n4. Associated fever, cough, or calf pain.",
    "Physical Exam": "1. Use of accessory muscles, tripod positioning.\n2. Auscultation: Wheezing (Asthma), Crackles (CHF/Pneumonia), Stridor (Upper airway).\n3. Jugular Venous Distension (JVD) and peripheral edema.",
    "Tests & Purpose": "1. ABGA/VBG: Assess PaO2, PaCO2, and pH status.\n2. BNP/NT-proBNP: Differentiate CHF from pulmonary causes.\n3. Chest X-ray: Evaluate for infiltrate, effusion, or edema.\n4. CTPA: If PE is suspected.",
    "Management": "1. Bronchodilators (Albuterol/Ipratropium) for obstructive disease.\n2. Nitroglycerin and Diuretics (Furosemide) for ADHF.\n3. Non-invasive Ventilation (BiPAP/CPAP) for acute respiratory failure.",
    "Consult & Disposition": "1. Pulmonology/Cardiology: For severe exacerbations or heart failure.\n2. ICU: For impending respiratory failure or required intubation.",
    "Discharge & Warning": "1. Discharge if symptoms resolve, SpO2 is stable on room air, and cause is treatable outpatient.\n2. Warning: Return for inability to speak in full sentences or cyanosis.",
    "Pearls & Pitfalls": "1. 'Silent chest' in a severe asthmatic is a sign of imminent respiratory arrest.\n2. Don't assume dyspnea is just anxiety; always rule out organic causes first."
  },
  {
    "Chief Complaint": "Palpitations",
    "Initial Action": "1. Immediate 12-lead EKG and continuous monitoring.\n2. Check Bedside Glucose (BST).\n3. IV access and assess hemodynamic stability.",
    "Red Flag Signs & Must-not-miss": "1. Ventricular Tachycardia (VT).\n2. Supraventricular Tachycardia (SVT) with hemodynamic compromise.\n3. Atrial Fibrillation with WPW (Rapid, irregular, wide).\n4. Acute Myocardial Ischemia.\n5. Electrolyte-induced arrhythmias (Hyperkalemia/Hypomagnesemia).",
    "Common Causes (Top 5)": "1. Sinus Tachycardia (Anxiety, Fever, Dehydration, Caffeine).\n2. Premature Atrial/Ventricular Contractions (PACs/PVCs).\n3. Supraventricular Tachycardia (PSVT).\n4. Atrial Fibrillation / Flutter.\n5. Hyperthyroidism.",
    "Key History": "1. Onset and offset (Sudden vs. Gradual).\n2. Duration and frequency of episodes.\n3. Associated syncope, chest pain, or SOB.\n4. Use of stimulants (Caffeine, nicotine, medications, drugs).",
    "Physical Exam": "1. Heart rate and rhythm (Regular vs. Irregular).\n2. Thyroid exam (Goiter).\n3. Signs of heart failure or anemia (Pallor).",
    "Tests & Purpose": "1. EKG: The definitive diagnostic tool (if captured during symptoms).\n2. CBC/Electrolytes: Screen for anemia and potassium/magnesium abnormalities.\n3. TFT (TSH/fT4): Rule out hyperthyroidism.",
    "Management": "1. Unstable: Immediate synchronized cardioversion.\n2. SVT: Vagal maneuvers, then Adenosine (6mg -> 12mg).\n3. AFib: Rate control (Diltiazem/Beta-blockers) and anticoagulation assessment.",
    "Consult & Disposition": "1. Cardiology: For new-onset AFib, sustained VT, or structural heart disease.\n2. Admission: Required for unstable rhythms or high-risk underlying causes.",
    "Discharge & Warning": "1. Discharge if rhythm is benign (Sinus, PACs) and workup is negative.\n2. Warning: Return for syncope, chest pain, or persistent rapid heart rate.",
    "Pearls & Pitfalls": "1. Patients often have normal EKGs in the ER; Holter monitoring/Event recorder follow-up is essential.\n2. Always check a pregnancy test in young women presenting with palpitations."
  },
  {
    "Chief Complaint": "Cardiopulmonary Arrest / DOA / CPR",
    "Initial Action": "1. Confirm pulselessness and initiate high-quality CPR.\n2. Attach Defibrillator; analyze rhythm (Shockable vs. Non-shockable).\n3. Secure advanced airway and obtain IV/IO access.",
    "Red Flag Signs & Must-not-miss": "1. Reversible Causes (H’s & T’s): Hypovolemia, Hypoxia, Hydrogen ion (Acidosis), Hypo/Hyperkalemia, Hypothermia; Tension pneumo, Tamponade, Toxins, Thrombosis (PE/MI).",
    "Common Causes (Top 5)": "1. Coronary Artery Disease (AMI).\n2. Respiratory Failure (Hypoxia).\n3. Hypovolemic Shock (Hemorrhage).\n4. Lethal Arrhythmias.\n5. Pulmonary Embolism.",
    "Key History": "1. Witnessed vs. Unwitnessed arrest.\n2. Bystander CPR and time to first shock.\n3. Preceding symptoms (Chest pain, SOB) and past medical history.\n4. Advance directives (DNR/DNI status).",
    "Physical Exam": "1. Absence of carotid pulse and spontaneous respirations.\n2. Signs of trauma or drug use (Track marks).\n3. Pupillary size and reactivity.",
    "Tests & Purpose": "1. ETCO2: Monitor CPR quality and detect ROSC (sudden rise).\n2. VBG/Electrolytes: Check for hyperkalemia or severe acidosis.\n3. Bedside Ultrasound: Identify cardiac activity, tamponade, or pneumothorax.",
    "Management": "1. Follow ACLS Algorithms (Epinephrine every 3-5 mins, Amiodarone for refractory VF/pVT).\n2. Defibrillation for VF/pVT.\n3. Targeted Temperature Management (TTM) post-ROSC.",
    "Consult & Disposition": "1. Cardiology: For emergent PCI if ROSC is achieved and MI is suspected.\n2. ICU: Post-cardiac arrest care.\n3. Ethics/Social Work: For family support and end-of-life decisions.",
    "Discharge & Warning": "1. N/A (Death or ICU admission).\n2. Communicate clearly with family regarding prognosis.",
    "Pearls & Pitfalls": "1. Minimize interruptions in chest compressions; even a 10-second pause significantly drops coronary perfusion pressure.\n2. Do not stop resuscitating a hypothermic patient until they are 'warm and dead'."
  },
  {
    "Chief Complaint": "Hypertension / 고혈압",
    "Initial Action": "1. Re-check BP in a quiet setting with appropriate cuff size.\n2. Assess for Target Organ Damage (TOD) symptoms.\n3. Continuous monitoring for hypertensive emergencies.",
    "Red Flag Signs & Must-not-miss": "1. Hypertensive Encephalopathy (AMS, Seizures).\n2. Acute Pulmonary Edema / MI.\n3. Aortic Dissection (Severe tearing pain).\n4. Preeclampsia / Eclampsia (Pregnant patients).\n5. Acute Renal Failure.",
    "Common Causes (Top 5)": "1. Essential HTN (Medication non-compliance).\n2. Secondary HTN (Pain, Anxiety, White-coat effect).\n3. Renal Parenchymal Disease.\n4. Medication/Drug induced (NSAIDs, Cocaine).\n5. Endocrine (Pheochromocytoma, Cushing's).",
    "Key History": "1. Baseline BP and current medications (Recent changes/omissions).\n2. Neurological (Headache, vision changes), Cardiac (Chest pain, SOB), Renal (Urine output) symptoms.\n3. Use of stimulants or sympathomimetics.",
    "Physical Exam": "1. Fundoscopy: Papilledema, hemorrhages, exudates (TOD).\n2. Neurological: Focal deficits, mental status.\n3. Cardiovascular: JVD, rales, new S3, peripheral pulses.",
    "Tests & Purpose": "1. UA: Check for proteinuria/hematuria (Renal TOD).\n2. BUN/Cr/Electrolytes: Evaluate kidney function.\n3. EKG: LVH or ischemic changes.\n4. Chest X-ray: For heart failure or widened mediastinum.",
    "Management": "1. Hypertensive Emergency: IV Nicardipine or Labetalol (Reduce MAP by max 25% in 1st hour).\n2. Hypertensive Urgency: Adjust oral meds; no benefit in rapid ER lowering.\n3. Aortic Dissection: Rapidly lower SBP to 100-120 and HR < 60.",
    "Consult & Disposition": "1. Admit for Hypertensive Emergencies (TOD present).\n2. Consult Neurology/Cardiology/Nephrology as needed based on TOD.",
    "Discharge & Warning": "1. Discharge asymptomatic Urgency with primary care follow-up.\n2. Warning: Return for severe headache, chest pain, vision loss, or confusion.",
    "Pearls & Pitfalls": "1. Do not aggressively lower BP in asymptomatic patients; rapid drops can cause cerebral ischemia.\n2. Pain and anxiety are the most common causes of transiently high BP in the ER."
  },
  {
    "Chief Complaint": "Hemoptysis / 객혈",
    "Initial Action": "1. Secure airway; consider early intubation with a large-diameter tube (≥8.0) for massive hemoptysis.\n2. Position the patient with the suspected bleeding side down (Lateral decubitus) to protect the non-bleeding lung.\n3. Suctioning and supplemental O2; ensure large-bore IV access and type/cross-match.",
    "Red Flag Signs & Must-not-miss": "1. Massive Hemoptysis (>100–600 mL/24hr): Risk of asphyxiation.\n2. Hypotension or Hypoxemia.\n3. Malignancy (Weight loss, smoking history, age).\n4. Anticoagulant use or coagulopathy.\n5. Pulmonary Embolism (Infarction causing hemoptysis).",
    "Common Causes (Top 5)": "1. Bronchitis (Most common).\n2. Bronchiectasis.\n3. Pneumonia.\n4. Lung Cancer.\n5. Tuberculosis (Especially in endemic areas).",
    "Key History": "1. Quantify the amount of blood (Teaspoon vs. Cup).\n2. Differentiate from pseudohemoptysis (Epistaxis) or hematemesis (GI bleed).\n3. History of smoking, TB exposure, or recent travel.\n4. Associated symptoms: Fever, pleuritic chest pain, weight loss.",
    "Physical Exam": "1. Examine the oropharynx and nares to rule out upper airway sources.\n2. Lung auscultation (Focal crackles or diminished sounds).\n3. Check for lymphadenopathy or finger clubbing.",
    "Tests & Purpose": "1. Chest X-ray: Screening for infiltrates, masses, or cavities.\n2. Chest CT (Contrast/Angio): Define source of bleeding and identify cancer/bronchiectasis.\n3. CBC/Coagulation: Assess anemia and bleeding risk.\n4. Sputum Culture/AFB: If TB or infection is suspected.",
    "Management": "1. Minor: Cough suppressants and treatment of underlying infection.\n2. Massive: Bronchial Artery Embolization (BAE) or emergency surgery.\n3. Anticoagulation reversal if necessary.",
    "Consult & Disposition": "1. Pulmonology/Thoracic Surgery: For massive or recurrent hemoptysis.\n2. Admission: Required for massive hemoptysis (ICU) or high-risk features.",
    "Discharge & Warning": "1. Discharge if hemodynamically stable and bleeding is scant/controlled.\n2. Warning: Return immediately for increased volume of blood or difficulty breathing.",
    "Pearls & Pitfalls": "1. Death in hemoptysis is usually due to asphyxiation (drowning in blood), not exsanguination; airway management is priority #1.\n2. Hemoptysis is typically alkaline (pH >7), whereas hematemesis is acidic (pH <3)."
  },
  {
    "Chief Complaint": "Headache / 두통",
    "Initial Action": "1. Assess mental status and focal neurological deficits.\n2. Check vitals (Identify severe hypertension).\n3. Provide analgesia and check Bedside Glucose (BST).",
    "Red Flag Signs & Must-not-miss": "1. Subarachnoid Hemorrhage (SAH): 'Thunderclap' onset.\n2. Meningitis/Encephalitis: Fever, altered mental status, neck stiffness.\n3. Intracranial Mass/Increased ICP: Worse in morning, papilledema.\n4. Temporal Arteritis (GCA): Age >50, jaw claudication, scalp tenderness.\n5. Carbon Monoxide Poisoning: Multiple people with same symptoms.",
    "Common Causes (Top 5)": "1. Tension-type Headache.\n2. Migraine.\n3. Cluster Headache.\n4. Viral Syndrome related headache.\n5. Medication Overuse (Rebound) headache.",
    "Key History": "1. Onset: Sudden/maximal at start (Thunderclap) is a major red flag.\n2. 'Worst headache of my life' or 'different from usual pattern'.\n3. Associated symptoms: Vomiting, photophobia, fever, visual changes.\n4. History of malignancy or HIV.",
    "Physical Exam": "1. Full Neurological Exam: Cranial nerves, motor/sensory, coordination, gait.\n2. Meningeal Signs: Brudzinski’s and Kernig’s signs.\n3. Fundoscopy: Check for papilledema.\n4. Temporal artery palpation.",
    "Tests & Purpose": "1. Non-contrast Brain CT: Detect acute hemorrhage (Highly sensitive within 6 hours of SAH onset).\n2. Lumbar Puncture (LP): If SAH is suspected but CT is negative, or to rule out meningitis.\n3. ESR/CRP: If Temporal Arteritis is suspected.",
    "Management": "1. Migraine: Triptans, Prochlorperazine, Ketorolac, IV fluids.\n2. Meningitis: Immediate empirical antibiotics and steroids.\n3. SAH: BP control and neurosurgical consult.",
    "Consult & Disposition": "1. Neurology/Neurosurgery: For organic/structural causes (Hemorrhage, tumor).\n2. Admission: Required for secondary headaches or refractory status migrainosus.",
    "Discharge & Warning": "1. Discharge if secondary causes are ruled out and pain is controlled.\n2. Warning: Return for sudden worsening, new focal deficits, or high fever.",
    "Pearls & Pitfalls": "1. Improvement of pain with analgesics does NOT rule out a serious underlying cause like SAH.\n2. For thunderclap headaches, a negative CT after 6 hours from onset may still require an LP."
  },
  {
    "Chief Complaint": "Seizure",
    "Initial Action": "1. Protect patient from injury; place in lateral decubitus to prevent aspiration.\n2. Check Bedside Glucose (BST) - Hypoglycemia must be ruled out immediately.\n3. If active (Status Epilepticus >5 mins), administer Benzodiazepines (e.g., Lorazepam 2–4 mg IV).",
    "Red Flag Signs & Must-not-miss": "1. Status Epilepticus: Convulsive or non-convulsive (High mortality).\n2. Intracranial Lesion: Hemorrhage, tumor, or abscess.\n3. CNS Infection: Meningitis or encephalitis.\n4. Eclampsia: Seizure in a pregnant patient (>20 weeks).\n5. Hyponatremia: Especially in elderly or marathon runners.",
    "Common Causes (Top 5)": "1. Subtherapeutic Antiepileptic Drug (AED) levels (Non-compliance).\n2. Alcohol Withdrawal.\n3. Metabolic issues (Hypoglycemia, Na+ imbalance).\n4. Stroke or old brain injury scar.\n5. Idiopathic (New-onset epilepsy).",
    "Key History": "1. Seizure semiology (Focal vs. Generalized) and duration.\n2. Post-ictal period: Duration of confusion/drowsiness.\n3. Compliance with AEDs and recent alcohol/drug use.\n4. Preceding 'aura' or history of head trauma.",
    "Physical Exam": "1. Signs of trauma (Head injury, posterior shoulder dislocation).\n2. Tongue biting (Lateral aspect is specific for generalized seizure).\n3. Focal neurological deficits (Todd’s Paralysis - temporary post-ictal deficit).",
    "Tests & Purpose": "1. BST and Electrolytes (Na, Ca, Mg): Rule out metabolic triggers.\n2. AED Serum Levels: Assess compliance/dosage.\n3. Brain CT: Required for first-ever seizure, trauma, or persistent AMS.\n4. LP: If fever or meningitis is suspected.",
    "Management": "1. Benzodiazepines for active seizures.\n2. Loading dose of AED (e.g., Levetiracetam, Fosphenytoin) for status or high recurrence risk.\n3. Magnesium Sulfate for Eclampsia.",
    "Consult & Disposition": "1. Neurology: For first-time seizure or poorly controlled epilepsy.\n2. Admission: For status epilepticus, structural lesions, or metabolic instability.",
    "Discharge & Warning": "1. Discharge if it's a known seizure disorder back to baseline with stable levels.\n2. Warning: No driving/operating machinery; return for recurrent seizures or inability to wake up.",
    "Pearls & Pitfalls": "1. A normal CT and normal labs in a first-time seizure still requires outpatient follow-up for EEG/MRI.\n2. Be wary of Pseudoseizures (PNES) but always treat as organic until proven otherwise."
  },
  {
    "Chief Complaint": "Stroke-like symptoms / 뇌졸중",
    "Initial Action": "1. Verify 'Last Known Normal' (LKN) time (Critical for thrombolysis/thrombectomy).\n2. Bedside Glucose (BST) - Hypoglycemia is the #1 stroke mimic.\n3. NIH Stroke Scale (NIHSS) assessment and 'Code Stroke' activation for STAT Non-con CT.",
    "Red Flag Signs & Must-not-miss": "1. Large Vessel Occlusion (LVO): High NIHSS, specific deficits (Gaze deviation, neglect).\n2. Intracranial Hemorrhage (ICH): Sudden onset, vomiting, headache, rapid AMS.\n3. Basilar Artery Thrombosis: Comatose patient, 'locked-in' syndrome, crossed signs.",
    "Common Causes (Top 5)": "1. Ischemic Stroke.\n2. Transient Ischemic Attack (TIA).\n3. Intracranial Hemorrhage (ICH).\n4. Hypoglycemia.\n5. Complex Migraine / Todd’s Paralysis.",
    "Key History": "1. Precise LKN time and onset pattern.\n2. Anticoagulant use (Warfarin, NOACs) - essential for tPA safety.\n3. Recent surgery, trauma, or bleeding history.\n4. Risk factors: AFib, HTN, Smoking, previous TIA.",
    "Physical Exam": "1. NIHSS: Standardized neurological assessment.\n2. Check for facial droop, arm drift, and abnormal speech (Cincinnati scale).\n3. Assess visual fields and extraocular movements.",
    "Tests & Purpose": "1. Non-contrast Brain CT: Rule out hemorrhage (pre-requisite for tPA).\n2. CT Angiography (CTA): Identify LVO for endovascular therapy (EVT).\n3. MRI/MRA (DWI): Detect early ischemia (superior to CT).",
    "Management": "1. Thrombolytics (tPA/TNK) if within 4.5 hours of LKN and no contraindications.\n2. Endovascular Thrombectomy (EVT) for LVO (up to 24 hours in selected cases).\n3. BP management (Keep <185/110 for tPA, or <220/120 if no tPA).",
    "Consult & Disposition": "1. Neurology/Neurosurgery/Interventional Radiology: Immediate consult.\n2. Admission: To Stroke Unit or ICU.",
    "Discharge & Warning": "1. Stroke/TIA should not be discharged from the ER without a full workup.\n2. Warning: Return immediately if symptoms return or worsen.",
    "Pearls & Pitfalls": "1. 'Time is Brain' - avoid delays for non-essential labs before the CT scan.\n2. Posterior circulation strokes can present only with vertigo/ataxia; maintain a high index of suspicion."
  },
  {
    "Chief Complaint": "Neck Pain / Stiffness / 목 통증",
    "Initial Action": "1. If trauma: Cervical collar immobilization and midline tenderness check.\n2. Assess airway and swallowing (Rule out deep neck space infection).\n3. Evaluate for focal neurological deficits in all four extremities.",
    "Red Flag Signs & Must-not-miss": "1. Meningitis: Triad of fever, neck stiffness, and AMS.\n2. Cervical Spine Fracture/Dislocation (Traumatic).\n3. Spinal Epidural Abscess: Fever, midline pain, IV drug use history.\n4. Carotid/Vertebral Artery Dissection: Neck pain + neurological deficit.\n5. Retropharyngeal Abscess: Drooling, stridor, 'tripod' position.",
    "Common Causes (Top 5)": "1. Cervical Strain / Sprain (Whiplash).\n2. Cervical Disc Herniation / Radiculopathy.\n3. Myofascial Pain Syndrome.\n4. Cervical Spondylosis (Degenerative).\n5. Tension-related muscle stiffness.",
    "Key History": "1. Mechanism of injury (High-speed MVC, fall).\n2. Fever, night sweats, or weight loss (Infection/Malignancy).\n3. Radicular symptoms: Numbness/weakness radiating down the arms.\n4. Anticoagulant use (Risk of epidural hematoma).",
    "Physical Exam": "1. Midline vertebral tenderness vs. paraspinal tenderness.\n2. Range of Motion (ROM): Proceed only if no midline tenderness (NEXUS criteria).\n3. Nuchal Rigidity: Resistance to passive flexion.\n4. Full motor/sensory/reflex exam of upper and lower limbs.",
    "Tests & Purpose": "1. C-spine CT: Gold standard for ruling out fracture in trauma.\n2. Brain CT & LP: If meningitis or SAH is suspected.\n3. MRI Neck: Essential for abscess, hematoma, or cord compression.",
    "Management": "1. Trauma: Maintain immobilization until cleared clinically or by imaging.\n2. Meningitis: Prompt IV antibiotics/steroids.\n3. Musculoskeletal: NSAIDs, heat, and gentle activity.",
    "Consult & Disposition": "1. Neurosurgery/Orthopedics: For fractures, cord compression, or instability.\n2. Admission: For meningitis, abscess, or unstable spine.",
    "Discharge & Warning": "1. Discharge if serious causes are ruled out and pain is manageable.\n2. Warning: Return for new weakness, numbness, difficulty urinating, or high fever.",
    "Pearls & Pitfalls": "1. Use NEXUS or Canadian C-spine Rules to avoid unnecessary imaging in low-risk trauma.\n2. Nuchal rigidity may be absent in the very young, very old, or immunocompromised patients with meningitis."
  },
  {
    "Chief Complaint": "Abdominal Pain / 복통",
    "Initial Action": "1. Assess vitals and evaluate for signs of shock (tachycardia, hypotension).\n2. Keep NPO; establish IV access and initiate fluid resuscitation if unstable.\n3. Perform pregnancy test (Urine hCG) for all females of childbearing age.",
    "Red Flag Signs & Must-not-miss": "1. Abdominal Aortic Aneurysm (AAA) Rupture: Pulsatile mass, back pain, shock.\n2. Mesenteric Ischemia: 'Pain out of proportion' to exam, history of AFib.\n3. Bowel Perforation: Rigid abdomen, rebound tenderness, free air on imaging.\n4. Ruptured Ectopic Pregnancy.\n5. Acute MI: Atypical presentation as epigastric pain.",
    "Common Causes (Top 5)": "1. Non-specific Abdominal Pain (NSAP).\n2. Appendicitis.\n3. Biliary Colic / Cholecystitis.\n4. Gastroenteritis.\n5. Urolithiasis (Renal Colic).",
    "Key History": "1. Onset (Sudden vs. Gradual) and progression (Migration of pain).\n2. Relation to meals and bowel habits.\n3. Previous surgical history (Risk for bowel obstruction).\n4. Associated symptoms: Fever, vomiting, melena, or hematuria.",
    "Physical Exam": "1. Palpate for peritonitis (Involuntary guarding, rebound tenderness).\n2. Auscultate for bowel sounds (Absent in ileus/perforation vs. high-pitched in obstruction).\n3. Examine for hernias (Incarcerated/Strangulated).\n4. Pelvic/Rectal exam as indicated.",
    "Tests & Purpose": "1. CBC, LFTs, Amylase/Lipase: Screen for infection, biliary, and pancreatic issues.\n2. Urine hCG: Rule out pregnancy complications.\n3. CT Abdomen/Pelvis (with/without contrast): Gold standard for most acute pathologies.\n4. Abdominal Ultrasound: Preferred for RUQ (Biliary) and Pelvic issues.",
    "Management": "1. Analgesia: Do not withhold pain meds (Opioids/NSAIDs); they do not mask the surgical exam.\n2. Anti-emetics and IV fluids.\n3. Empirical antibiotics for suspected peritonitis or sepsis.",
    "Consult & Disposition": "1. General Surgery: For 'Acute Abdomen' or surgical pathology (Appendicitis, Cholecystitis).\n2. Admission: For uncontrolled pain, inability to tolerate PO, or high-risk patients (elderly/immunocompromised).",
    "Discharge & Warning": "1. Discharge if pain is controlled, workup is negative, and patient can tolerate PO.\n2. Warning: Return for worsening pain, high fever, repeated vomiting, or syncope.",
    "Pearls & Pitfalls": "1. The 'Pain out of proportion' in Mesenteric Ischemia is a classic, high-yield pearl.\n2. Elderly patients may present with vague symptoms even in the presence of life-threatening pathology (e.g., no fever in perforated viscus)."
  },
  {
    "Chief Complaint": "Nausea & Vomiting / 구토",
    "Initial Action": "1. Assess hydration status and mental status (Risk of aspiration).\n2. Check Bedside Glucose (BST) to rule out DKA or hypoglycemia.\n3. Initiate IV rehydration and anti-emetics.",
    "Red Flag Signs & Must-not-miss": "1. Bowel Obstruction: Bilious vomiting, distension, surgical scars.\n2. Intracranial Pathology: Projectile vomiting, headache, papilledema.\n3. Diabetic Ketoacidosis (DKA): Kussmaul breathing, fruity odor, high glucose.\n4. Acute MI: Nausea as the primary symptom (especially in women/diabetics).\n5. Acute Poisoning / Overdose.",
    "Common Causes (Top 5)": "1. Viral Gastroenteritis.\n2. Food Poisoning.\n3. Medication Side Effects.\n4. Biliary Disease / Pancreatitis.\n5. Vestibular Disorders (Vertigo-associated).",
    "Key History": "1. Character of emesis (Bilious, bloody, or fecaloid).\n2. Relationship to food or travel.\n3. Last Menstrual Period (LMP) / Pregnancy risk.\n4. Associated symptoms: Diarrhea, constipation, or severe headache.",
    "Physical Exam": "1. Evaluate for dehydration (Dry mucous membranes, poor skin turgor).\n2. Abdominal exam for distension, tenderness, or succussion splash.\n3. Neurological exam for signs of increased ICP.",
    "Tests & Purpose": "1. Electrolytes, BUN/Cr: Assess metabolic alkalosis and renal function.\n2. UA: Check for ketones (DKA/Starvation) and UTI.\n3. Pregnancy test (hCG).\n4. EKG: To rule out atypical MI.",
    "Management": "1. Antiemetics (Ondansetron, Metoclopramide).\n2. Rehydration (Crystalloids).\n3. Correct electrolyte imbalances (e.g., Hypokalemia).",
    "Consult & Disposition": "1. Admission: For severe dehydration, intractable vomiting, or underlying surgical cause.\n2. Observation: For rehydration and trial of PO tolerance.",
    "Discharge & Warning": "1. Discharge after successful trial of PO fluids (clear liquids).\n2. Warning: Return if unable to keep down fluids, develops severe abdominal pain, or shows signs of dehydration (no urine).",
    "Pearls & Pitfalls": "1. Chronic vomiting? Consider Wernicke’s encephalopathy; give Thiamine before Glucose.\n2. Don't forget that N/V in a young child or infant can be the only sign of Intussusception."
  },
  {
    "Chief Complaint": "GI Bleeding (Upper and Lower) / 피토 혈변",
    "Initial Action": "1. Secure large-bore IV access (x2) and initiate rapid fluid resuscitation.\n2. Monitor vitals closely (Search for 'occult' shock: tachycardia before hypotension).\n3. Perform Type and Cross-match (Prep for transfusion).",
    "Red Flag Signs & Must-not-miss": "1. Variceal Bleeding: Massive hematemesis in patients with cirrhosis.\n2. Aortoenteric Fistula: 'Herald bleed' in patients with prior aortic graft.\n3. Boerhaave Syndrome: Esophageal rupture after forceful vomiting.\n4. Hemorrhagic Shock.\n5. Ischemic Colitis: Bloody diarrhea with severe pain.",
    "Common Causes (Top 5)": "1. Peptic Ulcer Disease (PUD).\n2. Esophageal Varices.\n3. Diverticulosis (Lower GI).\n4. Gastritis / Mallory-Weiss Tear.\n5. Hemorrhoids / Anal Fissures.",
    "Key History": "1. Color and consistency: Hematemesis, Melena (black/tarry), or Hematochezia (bright red).\n2. History of alcohol use, liver disease, or NSAID use.\n3. Weight loss or change in bowel habits (Malignancy).\n4. Use of anticoagulants or antiplatelets.",
    "Physical Exam": "1. Digital Rectal Exam (DRE): Essential to confirm blood and color.\n2. Evaluate for stigmata of chronic liver disease (Ascites, jaundice, caput medusae).\n3. Assess for orthostatic vitals if stable.",
    "Tests & Purpose": "1. Serial CBC: Monitor Hemoglobin (though initial Hb may be falsely normal in acute bleeds).\n2. BUN/Cr Ratio: >30 suggests Upper GI source (BUN increases due to blood protein digestion).\n3. Coagulation Profile (PT/INR): Assess for coagulopathy.",
    "Management": "1. Proton Pump Inhibitors (PPI): High-dose IV (e.g., Pantoprazole).\n2. Octreotide & Prophylactic Antibiotics: For suspected variceal bleeds.\n3. Blood transfusion: Goal Hb >7 g/dL (higher in active ischemia).",
    "Consult & Disposition": "1. Gastroenterology (GI): For emergent/urgent endoscopy (EGD/Colonoscopy).\n2. Admission: Usually to ICU or Step-down for active bleeding.",
    "Discharge & Warning": "1. Low-risk patients (Glasgow-Blatchford Score = 0) may be considered for outpatient.\n2. Warning: Return for syncope, increased bleeding, or severe abdominal pain.",
    "Pearls & Pitfalls": "1. A normal initial Hemoglobin level does NOT rule out a major acute bleed.\n2. NG tube aspiration is no longer routinely recommended for Upper GI bleed localization unless absolutely necessary."
  },
  {
    "Chief Complaint": "Diarrhea / 설사",
    "Initial Action": "1. Evaluate volume status and hemodynamic stability.\n2. Implement infection control (Contact precautions).\n3. Assess for electrolyte abnormalities (especially Hypokalemia).",
    "Red Flag Signs & Must-not-miss": "1. C. difficile Infection: Post-antibiotic use, toxic megacolon.\n2. Ischemic Colitis: Sudden pain followed by bloody diarrhea in the elderly.\n3. Hemolytic Uremic Syndrome (HUS): Bloody diarrhea + renal failure (especially kids).\n4. Mesenteric Ischemia.\n5. Toxic Megacolon: Fever, distension, and signs of sepsis.",
    "Common Causes (Top 5)": "1. Viral Gastroenteritis (Norovirus/Rotavirus).\n2. Food Poisoning (S. aureus, B. cereus).\n3. Bacterial Infection (Salmonella, Campylobacter).\n4. Medication side effects (Antibiotics, Metformin).\n5. Irritable Bowel Syndrome (IBS) exacerbation.",
    "Key History": "1. Duration, frequency, and character (Watery vs. Bloody/Mucoid).\n2. Recent travel, antibiotic use, or raw food consumption.\n3. Sick contacts or communal outbreaks.\n4. Associated fever, vomiting, or tenesmus.",
    "Physical Exam": "1. Abdominal tenderness or signs of peritonitis.\n2. Volume status: Skin turgor, mucous membranes, capillary refill.\n3. Skin: Look for rashes or petechiae (HUS/Sepsis).",
    "Tests & Purpose": "1. Electrolytes, BUN/Cr: Assess dehydration and AKI.\n2. Stool Studies (PCR/Culture): Only for severe, bloody, or persistent diarrhea (>7 days).\n3. C. diff Toxin Assay: For post-antibiotic or healthcare-associated diarrhea.",
    "Management": "1. Rehydration (PO preferred; IV if intractable vomiting/severe dehydration).\n2. Antimicrobials: Only for specific indications (e.g., severe travelers' diarrhea, C. diff).\n3. Avoid Loperamide in patients with high fever or bloody diarrhea (Inflammatory).",
    "Consult & Disposition": "1. Admission: For severe dehydration, electrolyte crisis, or toxic megacolon.\n2. Discharge: Most viral/mild bacterial cases.",
    "Discharge & Warning": "1. Discharge with hydration instructions (BRAT diet is less emphasized; focus on calories).\n2. Warning: Return for bloody stools, inability to keep down liquids, or high fever.",
    "Pearls & Pitfalls": "1. Elderly patients with 'diarrhea' might actually have fecal impaction with overflow diarrhea.\n2. Antibiotic-associated diarrhea without fever/leukocytosis is often just a side effect, not C. diff."
  },
  {
    "Chief Complaint": "Constipation / ",
    "Initial Action": "1. Assess for signs of bowel obstruction (Distension, vomiting).\n2. Perform Digital Rectal Exam (DRE) to evaluate for fecal impaction.\n3. Evaluate for systemic causes (Electrolytes, Neurological).",
    "Red Flag Signs & Must-not-miss": "1. Bowel Obstruction (SBO/LBO): Vomiting, obstipation (no gas), distension.\n2. Volvulus: Sudden onset, severe distension (common in elderly/institutionalized).\n3. Spinal Cord Compression / Cauda Equina: New constipation + saddle anesthesia.\n4. Hypercalcemia: 'Moans, groans, stones, and psychiatric overtones'.\n5. Colorectal Malignancy: Change in stool caliber, weight loss, anemia.",
    "Common Causes (Top 5)": "1. Functional / Idiopathic Constipation.\n2. Medication-induced (Opioids, Calcium-channel blockers, Anticholinergics).\n3. Fecal Impaction.\n4. Irritable Bowel Syndrome - Constipation predominant (IBS-C).\n5. Dehydration / Low fiber intake.",
    "Key History": "1. Baseline bowel habits vs. current frequency.\n2. Inability to pass flatus (Obstipation = red flag).\n3. Recent medication changes or iron supplementation.\n4. History of abdominal surgeries (Adhesion-related obstruction).",
    "Physical Exam": "1. Abdominal distension and tympany on percussion.\n2. DRE: Check for stool in the vault, consistency, masses, and anal tone.\n3. Neurological exam: Sensation and motor function if cord compression suspected.",
    "Tests & Purpose": "1. Abdominal X-ray (KUB): Assess stool burden and check for air-fluid levels (Obstruction).\n2. Electrolytes: Check for Hypercalcemia or Hypokalemia.\n3. CBC: Check for anemia (Occult malignancy).",
    "Management": "1. Enemas / Suppositories: For immediate relief in the ER.\n2. Laxatives: Bulk-forming, osmotic (PEG), or stimulant (Senna).\n3. Manual disimpaction if fecaloma is present (requires analgesia).",
    "Consult & Disposition": "1. Surgery: For Volvulus or Obstructive pathology.\n2. Discharge: Most functional cases after ER relief.",
    "Discharge & Warning": "1. Education on fiber, hydration, and exercise.\n2. Warning: Return for persistent vomiting, inability to pass gas, or severe pain.",
    "Pearls & Pitfalls": "1. Don't call it 'constipation' in an elderly patient with a distended abdomen until you've ruled out Volvulus or Obstruction.\n2. Opioid-induced constipation is best treated with stimulants + stool softeners, not just fiber."
  },
  {
    "Chief Complaint": "Jaundice / 황달",
    "Initial Action": "1. Assess vitals and evaluate for sepsis (e.g., Cholangitis).\n2. Check mental status for Hepatic Encephalopathy (Asterixis).\n3. Establish IV access and consider fluid resuscitation.",
    "Red Flag Signs & Must-not-miss": "1. Acute Cholangitis: Charcot’s Triad (Fever, Jaundice, RUQ pain) or Reynolds' Pentad (+AMS, Shock).\n2. Fulminant Hepatic Failure: Coagulopathy (INR >1.5) and encephalopathy.\n3. Hemolytic Anemia: Rapid drop in Hb with jaundice.\n4. Hepatorenal Syndrome: Acute renal failure in a cirrhotic patient.\n5. Painless Jaundice: Highly suspicious for pancreatic or biliary malignancy.",
    "Common Causes (Top 5)": "1. Alcoholic Liver Disease.\n2. Viral Hepatitis (A, B, C).\n3. Choledocholithiasis (Biliary obstruction).\n4. Drug-Induced Liver Injury (DILI) - e.g., Acetaminophen.\n5. Cirrhosis and its complications.",
    "Key History": "1. Presence of pain (Biliary colic vs. painless malignancy).\n2. Urine/Stool color changes (Dark urine, acholic stools).\n3. Recent medications, herbal supplements, and alcohol intake.\n4. Travel, blood transfusion, or sexual history (Hepatitis risk).\n5. Associated pruritus (Suggests obstructive cause).",
    "Physical Exam": "1. Scleral icterus and skin color.\n2. Stigmata of chronic liver disease (Spider angioma, caput medusae, ascites).\n3. Abdominal palpation for RUQ tenderness or Courvoisier’s sign (Palpable gallbladder).\n4. Neurological exam (Asterixis, AMS).",
    "Tests & Purpose": "1. LFTs (Total/Direct Bilirubin, AST/ALT, ALP, GGT): Differentiate hepatocellular vs. obstructive.\n2. CBC and PT/INR: Assess hepatic synthetic function and bleeding risk.\n3. Abdominal Ultrasound: First-line to check for biliary dilation/stones.\n4. MRCP/CT: Definitive imaging for obstructive causes.",
    "Management": "1. Immediate antibiotics for suspected cholangitis.\n2. Correct electrolyte imbalances and initiate IV fluids.\n3. Vitamin K supplementation if coagulopathic.",
    "Consult & Disposition": "1. GI/Surgery: For ERCP or surgical intervention in obstructive jaundice.\n2. Admission: For hepatic failure, cholangitis, or severe complications.",
    "Discharge & Warning": "1. Discharge if stable with known chronic liver disease or minor viral hepatitis (with follow-up).\n2. Warning: Return for confusion, bleeding, fever, or worsening abdominal pain.",
    "Pearls & Pitfalls": "1. Painless, progressive jaundice in an older patient is 'cancer until proven otherwise'.\n2. Do not assume jaundice is chronic in a known cirrhotic; look for acute triggers (infection, bleed, SBP)."
  },
  {
    "Chief Complaint": "Dysphagia / 삼킴곤란",
    "Initial Action": "1. Assess airway and risk of aspiration.\n2. Maintain NPO (Nothing by Mouth).\n3. Inspect oropharynx for visible foreign bodies.",
    "Red Flag Signs & Must-not-miss": "1. Airway Obstruction or Stridor.\n2. Esophageal Perforation (Boerhaave’s): Severe pain after vomiting.\n3. Acute Stroke: Neurological dysphagia with focal deficits.\n4. Deep Neck Space Infection (Retropharyngeal abscess).\n5. Esophageal Malignancy: Progressive dysphagia + weight loss.",
    "Common Causes (Top 5)": "1. GERD-related strictures.\n2. Esophageal Candidiasis (Common in immunocompromised).\n3. Esophageal Foreign Body (Food bolus).\n4. Post-stroke / Neurological dysphagia.\n5. Achalasia.",
    "Key History": "1. Solids vs. Liquids: Solids only suggests mechanical (stricture/tumor); both suggest motility (Achalasia).\n2. Speed of onset (Sudden vs. Gradual).\n3. Location of sensation (Oropharyngeal vs. Esophageal).\n4. Associated weight loss, heartburn, or chest pain.",
    "Physical Exam": "1. Neurological exam (Cranial nerves IX, X, XII).\n2. Neck exam for masses, lymphadenopathy, or crepitus.\n3. Observe for drooling or 'hot potato' voice.",
    "Tests & Purpose": "1. Neck/Chest X-ray: Check for foreign bodies or mediastinal air.\n2. Barium Swallow: Delineate strictures or motility disorders.\n3. CT Neck/Chest: If abscess or tumor is suspected.\n4. Endoscopy (EGD): Definitive diagnosis and potential foreign body removal.",
    "Management": "1. Supportive IV fluids and pain control.\n2. Glucagon (May help relax lower esophageal sphincter for food bolus, though controversial).\n3. Immediate endoscopy for sharp objects or button batteries.",
    "Consult & Disposition": "1. GI/ENT: For endoscopy or deep neck infection management.\n2. Neurology: For suspected stroke or neurogenic causes.",
    "Discharge & Warning": "1. Discharge if airway is safe and patient can tolerate liquids after minor resolution.\n2. Warning: Return for inability to swallow saliva, SOB, or fever.",
    "Pearls & Pitfalls": "1. If a patient cannot swallow their own saliva, they have a complete obstruction and need urgent endoscopy.\n2. Do not forget to check for 'button batteries' in pediatric cases."
  },
  {
    "Chief Complaint": "Flank Pain / 옆구리 통증",
    "Initial Action": "1. Check vitals (Rule out shock/hypotension).\n2. Provide analgesia (IV NSAIDs like Ketorolac are first-line).\n3. Bedside Glucose (BST).",
    "Red Flag Signs & Must-not-miss": "1. Ruptured Abdominal Aortic Aneurysm (AAA): Can mimic renal colic in older patients.\n2. Pyelonephritis with Sepsis.\n3. Renal Artery Occlusion / Infarction.\n4. Ovarian or Testicular Torsion (Referred pain).\n5. Pulmonary Embolism (Pleuritic pain radiating to flank).",
    "Common Causes (Top 5)": "1. Urolithiasis (Renal Colic).\n2. Acute Pyelonephritis (APN).\n3. Musculoskeletal Pain.\n4. Herpes Zoster (Pre-eruptive phase).\n5. Renal Cyst Rupture or Hemorrhage.",
    "Key History": "1. Quality of pain: Sudden, colicky, and severe suggests stones.\n2. Radiation: Down to groin or genitals suggests ureteral stone.\n3. Associated symptoms: Hematuria, frequency, fever, or chills.\n4. Previous history of stones.",
    "Physical Exam": "1. Costovertebral Angle Tenderness (CVAT).\n2. Abdominal palpation for pulsatile mass (AAA).\n3. Genital exam (Must rule out torsion in males).",
    "Tests & Purpose": "1. UA (Urinalysis): Check for hematuria (stones) or pyuria (infection).\n2. Non-contrast CT Abdomen/Pelvis (Stone CT): Gold standard for stones.\n3. BUN/Cr: Evaluate renal function.\n4. CBC/CRP: Assess for infection.",
    "Management": "1. NSAIDs (superior to opioids for ureteral spasm).\n2. Hydration (IV fluids).\n3. Antibiotics if infection is suspected.",
    "Consult & Disposition": "1. Urology: For large stones (>6-10mm), persistent pain, or obstructive infection.\n2. Admission: For sepsis, intractable pain, or solitary kidney with stone.",
    "Discharge & Warning": "1. Discharge if pain is controlled and stone is small (<5mm) without infection.\n2. Warning: Return for inability to urinate (anuria), high fever, or worsening pain.",
    "Pearls & Pitfalls": "1. **Crucial:** Always rule out AAA in a patient >50 with new-onset flank pain before assuming it's a stone."
  },
  {
    "Chief Complaint": "Vaginal Bleeding / 질출혈",
    "Initial Action": "1. **Pregnancy Test (Urine hCG) - Mandatory.**\n2. Assess vitals and evaluate for hemorrhagic shock.\n3. Establish large-bore IV and start fluid resuscitation if unstable.",
    "Red Flag Signs & Must-not-miss": "1. Ruptured Ectopic Pregnancy.\n2. Placental Abruption (Third trimester).\n3. Placenta Previa (Painless bleeding in late pregnancy).\n4. Incomplete/Septic Abortion.\n5. Uterine Rupture or Laceration.",
    "Common Causes (Top 5)": "1. Abnormal Uterine Bleeding (AUB) - Non-gestational.\n2. Pregnancy-related (Miscarriage).\n3. Uterine Leiomyoma (Fibroids).\n4. PID or Cervicitis.\n5. OCP-related breakthrough bleeding.",
    "Key History": "1. LMP (Last Menstrual Period) and pregnancy status.\n2. Volume of bleeding (Count pads/tampons per hour).\n3. Associated pain (Sudden, severe pain suggests ectopic or abruption).\n4. History of trauma or sexual assault.",
    "Physical Exam": "1. Pelvic exam (Speculum): Identify source (Vaginal, cervical, or uterine).\n2. Bimanual exam: Check for CMT (Cervical Motion Tenderness) or adnexal masses.\n3. Assess for skin pallor or orthostasis.",
    "Tests & Purpose": "1. hCG (Urine/Serum): Rule out pregnancy complications.\n2. CBC: Assess degree of anemia.\n3. Pelvic Ultrasound (TVUS): Locate pregnancy or identify fibroids/cysts.\n4. Type and Screen: Prepare for possible transfusion.",
    "Management": "1. Stabilize with fluids/blood if unstable.\n2. Management of miscarriage (Medical vs. Surgical).\n3. Hormonal therapy (Estrogen/Progestin) for AUB if stable.",
    "Consult & Disposition": "1. OB/GYN: For all pregnancy-related bleeding or heavy AUB.\n2. Admission: For ruptured ectopic, septic abortion, or hemorrhagic shock.",
    "Discharge & Warning": "1. Discharge if stable, non-gestational or early stable miscarriage.\n2. Warning: Return for syncope, soaking >1 pad per hour, or severe abdominal pain.",
    "Pearls & Pitfalls": "1. Any female of childbearing age with vaginal bleeding/pain is an ectopic pregnancy until proven otherwise."
  },
  {
    "Chief Complaint": "Pelvic Pain / 골반통",
    "Initial Action": "1. **Urine hCG.**\n2. Assess vitals and check for peritoneal signs.\n3. Provide analgesia.",
    "Red Flag Signs & Must-not-miss": "1. Ruptured Ectopic Pregnancy.\n2. Ovarian Torsion (Surgical emergency).\n3. Tubo-ovarian Abscess (TOA) Rupture.\n4. Acute Appendicitis.\n5. Ruptured Ovarian Cyst with Hemoperitoneum.",
    "Common Causes (Top 5)": "1. Pelvic Inflammatory Disease (PID).\n2. Ruptured Ovarian Cyst (Simple).\n3. Dysmenorrhea.\n4. UTI / Cystitis.\n5. Endometriosis.",
    "Key History": "1. Onset: Sudden (Torsion/Rupture) vs. Gradual (PID/Infection).\n2. Relation to menstrual cycle.\n3. Sexual history and vaginal discharge.\n4. History of prior cysts or surgeries.",
    "Physical Exam": "1. Abdominal exam for rebound/guarding.\n2. Pelvic exam: CMT (Chandelier sign) and adnexal tenderness.\n3. Check for fever.",
    "Tests & Purpose": "1. hCG: Rule out pregnancy.\n2. UA: Rule out UTI/Cystitis.\n3. Pelvic Ultrasound (with Doppler): Evaluate for torsion (blood flow) and masses.\n4. STD Swabs: Screen for GC/CT.",
    "Management": "1. Empirical antibiotics for PID (Ceftriaxone + Doxycycline).\n2. Surgical consult for torsion or ruptured ectopic.\n3. Pain management.",
    "Consult & Disposition": "1. OB/GYN: For torsion, TOA, or ectopic pregnancy.\n2. Admission: For surgical pathology or severe PID (cannot tolerate PO).",
    "Discharge & Warning": "1. Discharge if stable PID or simple cyst with follow-up.\n2. Warning: Return for worsening pain, high fever, or fainting.",
    "Pearls & Pitfalls": "1. Normal blood flow on Doppler does **not** 100% rule out ovarian torsion; clinical suspicion is key."
  },
  {
    "Chief Complaint": "Hematuria / 혈뇨",
    "Initial Action": "1. Assess vitals and check for signs of hemorrhagic shock in massive hematuria.\n2. Evaluate for bladder outlet obstruction; if 'Clot Retention' is present, insert a large-bore (20-22Fr) 3-way Foley catheter for continuous bladder irrigation (CBI).\n3. Establish IV access and provide fluid resuscitation.",
    "Red Flag Signs & Must-not-miss": "1. Massive Hematuria with Clot Retention (Urological emergency).\n2. Malignancy: Especially painless gross hematuria in patients >40 or smokers.\n3. Glomerulonephritis: Associated with HTN, edema, and RBC casts.\n4. Traumatic Renal/Bladder Injury.\n5. Coagulopathy: Spontaneous bleeding due to supratherapeutic anticoagulation.",
    "Common Causes (Top 5)": "1. Urinary Tract Infection (UTI / Cystitis).\n2. Urolithiasis (Renal/Ureteral stones).\n3. Benign Prostatic Hyperplasia (BPH).\n4. Bladder or Renal Neoplasm.\n5. Trauma (latrogenic or external).",
    "Key History": "1. Painful vs. Painless: Painless is high risk for malignancy; painful suggests infection or stones.\n2. Timing of hematuria: Initial (Urethral), Terminal (Bladder neck/Prostate), or Total (Bladder/Ureter/Kidney).\n3. History of smoking or occupational exposure to dyes/chemicals.\n4. Use of anticoagulants or recent vigorous exercise.",
    "Physical Exam": "1. Costovertebral Angle Tenderness (CVAT) and suprapubic tenderness.\n2. DRE: Check for prostate size, nodules, or tenderness.\n3. Skin: Look for petechiae or ecchymosis (Systemic bleeding disorder).",
    "Tests & Purpose": "1. UA/Microscopy: Confirm RBCs (>3/hpf) and rule out pseudohematuria (beets, meds).\n2. BUN/Cr: Evaluate for acute kidney injury.\n3. CBC/Coagulation: Assess blood loss and bleeding diathesis.\n4. CT Urogram: For comprehensive evaluation of stones and tumors.",
    "Management": "1. CBI (Continuous Bladder Irrigation) for clot-related obstruction.\n2. Antibiotics for UTI.\n3. Correct any underlying coagulopathy.",
    "Consult & Disposition": "1. Urology: For clot retention, gross hematuria, or suspected malignancy.\n2. Admission: For intractable bleeding, urosepsis, or AKI.",
    "Discharge & Warning": "1. Discharge if stable and urine flow is maintained with follow-up.\n2. Warning: Return for inability to void, worsening pain, or dizziness.",
    "Pearls & Pitfalls": "1. Do not assume hematuria is due to anticoagulants; malignancy must still be ruled out.\n2. Gross hematuria in a trauma patient requires a CT with IV contrast (delayed phase) to check for collecting system injury."
  },
  {
    "Chief Complaint": "Dysuria / Urinary Retention / 배뇨곤란",
    "Initial Action": "1. Bedside Bladder Scan to quantify residual volume (Significant if >300-400 mL).\n2. Urgent decompression with a urethral catheter (Foley).\n3. Check vitals for signs of urosepsis.",
    "Red Flag Signs & Must-not-miss": "1. Cauda Equina Syndrome: Retention + saddle anesthesia + decreased anal tone.\n2. Urosepsis: Retention with fever and hypotension.\n3. Prostatic Abscess: Severe pain and fluctuance on DRE.\n4. Spinal Cord Compression / Injury.",
    "Common Causes (Top 5)": "1. Benign Prostatic Hyperplasia (BPH) - Most common in males.\n2. UTI / Prostatitis.\n3. Medication-induced (Anticholinergics, Alpha-agonists, Sympathomimetics).\n4. Urethral Stricture.\n5. Neurogenic bladder.",
    "Key History": "1. New neurological symptoms (Weakness, numbness).\n2. Recent medication changes (e.g., Cold/allergy meds).\n3. Previous history of urethral instrumentation or STIs.\n4. Presence of fever or chills.",
    "Physical Exam": "1. Palpate for a distended bladder in the suprapubic area.\n2. DRE: Assess prostate and check for anal tone (Critical neuro screen).\n3. Neuro exam: Focus on lower extremity motor/sensory and reflexes.",
    "Tests & Purpose": "1. UA/UC: Rule out infection.\n2. BUN/Cr: Check for post-renal AKI (Obstructive uropathy).\n3. PSA (Optional): Not recommended in acute phase (will be falsely elevated).",
    "Management": "1. Catheterization (Coude tip may be needed for BPH).\n2. Alpha-blockers (Tamsulosin) to facilitate voiding trials.\n3. Antibiotics if prostatitis or UTI is suspected.",
    "Consult & Disposition": "1. Urology: For difficult catheterization or prostatic abscess.\n2. Admission: For urosepsis, significant AKI, or neurological cause.",
    "Discharge & Warning": "1. Discharge with a leg-bag and Urology follow-up in 48-72h.\n2. Warning: Return for fever, vomiting, or if the catheter stops draining.",
    "Pearls & Pitfalls": "1. Always ask about 'saddle anesthesia'—don't miss the surgical emergency of Cauda Equina."
  },
  {
    "Chief Complaint": "Scrotal Pain / Swelling / 고환",
    "Initial Action": "1. Immediate assessment for Testicular Torsion (Time-sensitive: 6-hour window).\n2. Keep NPO if torsion is suspected (Prepare for surgery).\n3. Provide analgesia and consider scrotal elevation.",
    "Red Flag Signs & Must-not-miss": "1. Testicular Torsion: Sudden onset, high-riding testis, absent cremasteric reflex.\n2. Fournier’s Gangrene: Necrotizing fasciitis of the perineum; crepitus, systemic toxicity.\n3. Incarcerated Inguinal Hernia.\n4. Scrotal Abscess.",
    "Common Causes (Top 5)": "1. Epididymitis / Orchitis.\n2. Torsion of the Testicular Appendage (Blue dot sign).\n3. Hydrocele / Varicocele (Painless swelling).\n4. Trauma (Hematocele).\n5. Testicular Tumor (Painless mass).",
    "Key History": "1. Onset: Sudden (Torsion) vs. Gradual (Epididymitis).\n2. Associated fever or urinary symptoms.\n3. Sexual history (GC/CT risk in younger males).\n4. History of recent trauma or heavy lifting.",
    "Physical Exam": "1. Cremasteric Reflex: Present in epididymitis, usually absent in torsion.\n2. Prehn's Sign: Relief with elevation (Suggests epididymitis, unreliable for torsion).\n3. Transillumination: For hydrocele evaluation.",
    "Tests & Purpose": "1. Color Doppler Ultrasound: Evaluate testicular blood flow (Gold standard).\n2. UA/UC: Check for associated UTI.\n3. STD Swabs: If epididymitis is suspected in sexually active males.",
    "Management": "1. Torsion: Manual detorsion (Open book technique) while waiting for surgery.\n2. Fournier’s: Aggressive fluid resuscitation, broad-spectrum IV antibiotics, and emergent debridement.\n3. Epididymitis: Antibiotics (Ceftriaxone + Doxycycline).",
    "Consult & Disposition": "1. Urology: Immediate for torsion or Fournier's.\n2. Surgery: For incarcerated hernia.",
    "Discharge & Warning": "1. Discharge for minor infections with scrotal support and follow-up.\n2. Warning: Return for worsening pain, skin discoloration, or high fever.",
    "Pearls & Pitfalls": "1. Don't let a normal ultrasound delay a surgical consult if clinical suspicion for torsion is high."
  },
  {
    "Chief Complaint": "Pain in Pregnancy / 임신",
    "Initial Action": "1. Check vitals and Fetal Heart Tones (FHT) (Normal: 110-160 bpm).\n2. Place patient in Left Lateral Decubitus position (to relieve IVC compression).\n3. Establish IV access if hemorrhage or shock is suspected.",
    "Red Flag Signs & Must-not-miss": "1. Placental Abruption: Painful bleeding, rigid uterus.\n2. Ruptured Ectopic Pregnancy: Sudden pain, syncope, (+)hCG.\n3. Preeclampsia / Eclampsia: HTN, headache, epigastric pain.\n4. Uterine Rupture.\n5. Preterm Labor.",
    "Common Causes (Top 5)": "1. Round Ligament Pain.\n2. UTI / Pyelonephritis (Common trigger for contractions).\n3. Braxton-Hicks Contractions.\n4. Miscarriage (Threatened/Inevitable).\n5. Appendicitis (Note: Appendix moves upward in pregnancy).",
    "Key History": "1. Gestational age (GA) and obstetric history (GTPAL).\n2. Presence of vaginal bleeding or leakage of fluid (PROM).\n3. Fetal movement changes.\n4. Presence of headache or visual changes (Pre-eclampsia).",
    "Physical Exam": "1. Abdominal exam: Assess for fundal height and uterine tenderness.\n2. Speculum exam: Check for cervical dilation or pooling of fluid.\n3. Pelvic exam: Bimanual (If placenta previa is ruled out by US).",
    "Tests & Purpose": "1. Pelvic US: Assess fetal viability, placental location, and amniotic fluid.\n2. UA: Check for proteinuria (Preeclampsia) or infection.\n3. CBC/Coag/Type & Screen: If bleeding is present.\n4. Kleihauer-Betke (KB) test: If trauma is the cause (check for feto-maternal hemorrhage).",
    "Management": "1. RhoGAM for Rh-negative patients with bleeding.\n2. Magnesium Sulfate for eclampsia or neuroprotection.\n3. Tocolytics vs. Induction based on GA and cause.",
    "Consult & Disposition": "1. OB/GYN: Immediate consult for all pregnancy-related pain.\n2. Admission: For any signs of maternal/fetal distress or labor.",
    "Discharge & Warning": "1. Discharge if pain is benign and FHT is reassuring.\n2. Warning: Return for bleeding, fluid leak, decreased fetal movement, or severe headache.",
    "Pearls & Pitfalls": "1. Always rule out non-obstetric causes like appendicitis or cholecystitis, but assume obstetric emergency first."
  },
  {
    "Chief Complaint": "Back Pain (Traumatic focus) / 요통",
    "Initial Action": "1. Evaluate for 'Red Flags' (Cauda Equina, Infection, AAA).\n2. Perform a focused neurological exam (Strength, sensation, reflexes).\n3. Assess for midline bony tenderness.",
    "Red Flag Signs & Must-not-miss": "1. Cauda Equina Syndrome: Saddle anesthesia, bowel/bladder dysfunction.\n2. Spinal Epidural Abscess: Fever + Focal pain + IV drug use.\n3. Ruptured AAA: Back pain with hypotension/pulsatile mass.\n4. Vertebral Osteomyelitis.\n5. Pathological Fracture (Malignancy).",
    "Common Causes (Top 5)": "1. Lumbar Strain / Musculoskeletal Pain.\n2. Herniated Nucleus Pulposus (HNP).\n3. Spinal Stenosis.\n4. Vertebral Compression Fracture (Osteoporosis).\n5. Sciatica.",
    "Key History": "1. Mechanism of injury: Fall from height, MVC, or direct blow.\n2. Weight loss or history of cancer.\n3. Incontinence (Urinary or Fecal).\n4. Anticoagulant use (Risk for spinal hematoma).",
    "Physical Exam": "1. Straight Leg Raise (SLR): Check for radiculopathy.\n2. Midline Vertebral Tenderness (Indicator for imaging in trauma).\n3. DRE: Check for sphincter tone and perianal sensation.",
    "Tests & Purpose": "1. **Imaging Rules for C-Spine (Applied to Back trauma logic):**\n   - **Canadian C-Spine Rule:** Assess High-risk factors (Age >65, dangerous mechanism, paresthesia), Low-risk factors (Simple rearend, sitting position, ambulatory), and ability to rotate neck.\n   - **NEXUS Criteria:** No imaging if: No midline tenderness, No intoxication, Normal alertness, No focal neuro deficit, No painful distracting injury.\n2. **X-ray Views (Trauma):**\n   - **C-Spine:** AP, Lateral, Open-mouth Odontoid (Check for alignment/fracture).\n   - **L-Spine:** AP, Lateral (Check for compression or burst fractures).\n3. **MRI:** Gold standard for Cauda Equina, Abscess, or Cord Compression.",
    "Management": "1. Conservative: NSAIDs, heat, and early mobilization.\n2. Acute Cord Compression: High-dose steroids (Dexamethasone) and Neurosurgery consult.\n3. Antibiotics for abscess or osteomyelitis.",
    "Consult & Disposition": "1. Neurosurgery / Orthopedics: For instability, fractures, or neuro deficits.\n2. Admission: For surgical emergencies, intractable pain, or systemic infection.",
    "Discharge & Warning": "1. Discharge with analgesia and activity instructions if workup is negative.\n2. Warning: Return for saddle anesthesia, leg weakness, or loss of bladder control.",
    "Pearls & Pitfalls": "1. Do not miss an AAA in an elderly patient presenting with 'back pain'.\n2. 'Pain out of proportion' in a back pain patient with a fever is Spinal Epidural Abscess until proven otherwise."
  },
  {
    "Chief Complaint": "Limb Pain / Swelling / 사지 통증",
    "Initial Action": "1. Assess neurovascular status: Check distal pulses, capillary refill, and sensation.\n2. Evaluate for 'Hard Signs' of vascular injury or Compartment Syndrome (The 6 Ps).\n3. Elevate the limb and provide analgesia.",
    "Red Flag Signs & Must-not-miss": "1. Compartment Syndrome: Pain out of proportion, pain with passive stretch (earliest sign).\n2. Deep Vein Thrombosis (DVT) / Pulmonary Embolism (PE).\n3. Acute Arterial Occlusion: Sudden cold, pale, pulseless limb.\n4. Necrotizing Fasciitis: Dishwater discharge, crepitus, systemic toxicity.\n5. Phlegmasia Cerulea Dolens: Massive DVT causing arterial compromise.",
    "Common Causes (Top 5)": "1. Cellulitis.\n2. Muscle Strain / Ligamentous Sprain.\n3. Venous Insufficiency / Lymphedema.\n4. Deep Vein Thrombosis (DVT).\n5. Superficial Thrombophlebitis.",
    "Key History": "1. History of trauma or prolonged immobilization (DVT risk).\n2. Speed of onset: Sudden (Embolus/Trauma) vs. Gradual (Infection/DVT).\n3. Presence of fever or systemic symptoms.\n4. Risk factors: Cancer, recent surgery, or smoking.",
    "Physical Exam": "1. Measurement of limb circumference (Asymmetry >3cm in DVT).\n2. Palpation of compartments for tenseness.\n3. Skin temperature and color comparison.",
    "Tests & Purpose": "1. **Duplex Ultrasound:** Identify DVT or arterial flow.\n2. **D-dimer:** Rule out DVT/PE in low-risk patients (Wells criteria).\n3. **Compartment Pressure Measurement:** If compartment syndrome is clinically suspected.\n4. **CK / Myoglobin:** Assess for Rhabdomyolysis in crush injuries.\n5. **X-ray Views:** AP and Lateral of the bone/joint involved (Include joint above and below if traumatic).",
    "Management": "1. DVT: Anticoagulation (Heparin/LMWH/NOACs).\n2. Compartment Syndrome: Immediate surgical fasciotomy.\n3. Cellulitis: Targeted antibiotics.",
    "Consult & Disposition": "1. Orthopedics: For compartment syndrome.\n2. Vascular Surgery: For arterial occlusion.\n3. Admission: For limb-threatening conditions or systemic infection.",
    "Discharge & Warning": "1. Discharge if stable DVT or cellulitis with follow-up.\n2. Warning: Return for sudden chest pain (PE), worsening pain, or limb numbness.",
    "Pearls & Pitfalls": "1. Do not rely on pulses to rule out Compartment Syndrome; pulses are often present until late stages."
  },
  {
    "Chief Complaint": "Joint Pain / Swelling / 관절 통증",
    "Initial Action": "1. Assess Range of Motion (ROM): Passive vs. Active.\n2. Check for systemic signs: Fever or multiple joint involvement.\n3. Splint and provide analgesia if traumatic.",
    "Red Flag Signs & Must-not-miss": "1. Septic Arthritis: Medical emergency; can destroy a joint in 24 hours.\n2. Crystal Arthropathy (Gout/Pseudogout).\n3. Hemarthrosis: In trauma or patients on anticoagulants.\n4. Rheumatic Fever / Lyme Disease.\n5. Gonococcal Arthritis: Tenosynovitis, dermatitis, polyarthralgia.",
    "Common Causes (Top 5)": "1. Osteoarthritis (OA) exacerbation.\n2. Gout / Pseudogout.\n3. Bursitis / Tendonitis.\n4. Trauma (Sprain/Ligamentous tear).\n5. Rheumatoid Arthritis (RA).",
    "Key History": "1. Sudden vs. Gradual onset.\n2. Monoarticular (one joint) vs. Polyarticular (many joints).\n3. History of similar episodes (Gout).\n4. Recent infection (Reactive/Septic) or trauma.",
    "Physical Exam": "1. Joint Effusion: Check for fluctuance or ballottement.\n2. Erythema, warmth, and tenderness.\n3. Neurovascular check distal to the joint.",
    "Tests & Purpose": "1. **Arthrocentesis (Synovial Fluid Analysis):** Cell count, Gram stain, culture, and crystal analysis (Essential for ruling out Septic Arthritis).\n2. **X-ray Views:** AP and Lateral (and Sunrise/Axial for specific joints like knee/shoulder).\n3. **ESR/CRP/Uric Acid:** Inflammatory markers.",
    "Management": "1. Septic Arthritis: IV antibiotics and surgical drainage/washout.\n2. Gout: NSAIDs, Colchicine, or Steroids.\n3. OA/Strain: RICE (Rest, Ice, Compression, Elevation).",
    "Consult & Disposition": "1. Orthopedics: For septic arthritis or ligamentous injury requiring surgery.\n2. Rheumatology: For complex autoimmune arthropathies.",
    "Discharge & Warning": "1. Discharge if septic arthritis is ruled out and pain is controlled.\n2. Warning: Return for new fever, inability to bear weight, or worsening swelling.",
    "Pearls & Pitfalls": "1. Septic arthritis can occur in a joint already affected by Gout or OA; 'Gout' history does not rule out infection."
  },
  {
    "Chief Complaint": "Fall / 낙상",
    "Initial Action": "1. Immediate C-spine stabilization if trauma suspected.\n2. Assess ABCs and GCS.\n3. Identify the 'Mechanical' vs. 'Medical' cause (e.g., Syncope, Stroke).",
    "Red Flag Signs & Must-not-miss": "1. Intracranial Hemorrhage (especially in elderly on anticoagulants).\n2. Cervical Spine Fracture.\n3. Hip Fracture (High morbidity in elderly).\n4. Occult MI / Arrhythmia causing the fall.\n5. Rhabdomyolysis (from 'long lie' on the floor).",
    "Common Causes (Top 5)": "1. Mechanical Trip/Slip.\n2. Orthostatic Hypotension.\n3. Syncope (Cardiac vs. Vasovagal).\n4. Medication Side Effects (Benzodiazepines, Antihypertensives).\n5. Frailty / Gait instability.",
    "Key History": "1. Pre-fall symptoms: Dizziness, chest pain, palpitations.\n2. LOC (Loss of Consciousness) and duration.\n3. Anticoagulant/Antiplatelet use.\n4. Environmental factors.",
    "Physical Exam": "1. Head-to-toe trauma survey.\n2. Orthostatic vitals.\n3. Neurological exam: Focus on focal deficits and gait.\n4. Extremities: Look for shortening/external rotation (Hip fx).",
    "Tests & Purpose": "1. **Imaging Rules:**\n   - **Canadian C-Spine Rule / NEXUS Criteria:** To determine the need for C-spine imaging.\n   - **Canadian CT Head Rule:** To determine the need for CT in minor head injury.\n2. **X-ray Views:**\n   - **Hip:** AP Pelvis, AP and Cross-table Lateral of the hip.\n   - **Chest:** Upright PA/Lateral (if medical cause suspected).\n3. **EKG:** Rule out arrhythmia/ischemia.\n4. **BST / Electrolytes:** Rule out hypoglycemia/hyponatremia.",
    "Management": "1. Stabilize fractures and manage pain.\n2. Correct medical triggers (Dehydration, electrolyte imbalance).\n3. Trauma management for identified injuries.",
    "Consult & Disposition": "1. Orthopedics: For fractures.\n2. Cardiology/Neurology: Based on medical cause.\n3. Admission: For serious injury, high-risk elderly, or 'failure to thrive'.",
    "Discharge & Warning": "1. Discharge if injuries are minor and cause is benign/resolved.\n2. Warning: Return for confusion, severe pain, or recurrent falls.",
    "Pearls & Pitfalls": "1. In the elderly, a fall is often a sign of an underlying illness (UTI, Sepsis, or MI)."
  },
  {
    "Chief Complaint": "Head Trauma / 두부 외상",
    "Initial Action": "1. ABCs and C-spine immobilization.\n2. Assess Glasgow Coma Scale (GCS).\n3. Check for signs of increased ICP (Cushing's triad).",
    "Red Flag Signs & Must-not-miss": "1. Epidural Hematoma: 'Lucid interval' followed by rapid decline.\n2. Subdural Hematoma: Common in elderly/alcoholics.\n3. Basilar Skull Fracture: Battle’s sign, Raccoon eyes, CSF rhinorrhea/otorrhea.\n4. Traumatic Brain Injury (TBI) / Axonal Injury.\n5. Post-traumatic Seizures.",
    "Common Causes (Top 5)": "1. Falls.\n2. Motor Vehicle Collisions (MVC).\n3. Assaults.\n4. Sports Injuries.\n5. Industrial Accidents.",
    "Key History": "1. Mechanism: High-speed, fall from >3ft (or 5 stairs).\n2. Loss of Consciousness (LOC) and Post-traumatic Amnesia (PTA).\n3. Anticoagulant use (Highest risk factor for delayed hemorrhage).\n4. Presence of vomiting or severe headache.",
    "Physical Exam": "1. Scalp: Hematoma, laceration, or palpated skull step-off.\n2. Pupils: Symmetry and reactivity.\n3. Lateralizing signs: Hemiparesis or decerebrate/decorticate posturing.",
    "Tests & Purpose": "1. **Imaging Rules:**\n   - **Canadian CT Head Rule:** Apply to patients with GCS 13-15 to determine the need for CT (Criteria: Age >65, vomiting x2, suspected skull fx, etc.).\n   - **NEXUS:** To rule out C-spine injury.\n2. **CT Brain (Non-contrast):** Gold standard for acute hemorrhage.\n3. **C-Spine CT:** Often performed concurrently with Head CT in trauma.",
    "Management": "1. Maintain Cerebral Perfusion Pressure (CPP).\n2. Mannitol / Hypertonic Saline: For suspected herniation.\n3. Elevate head of bed to 30 degrees.",
    "Consult & Disposition": "1. Neurosurgery: For any intracranial hemorrhage or depressed fracture.\n2. Admission: For GCS <15, hemorrhage, or persistent vomiting.",
    "Discharge & Warning": "1. Discharge if CT is negative and symptoms are mild, provided a caregiver is present.\n2. Warning: Return for worsening headache, confusion, repeated vomiting, or seizure.",
    "Pearls & Pitfalls": "1. Patients on Warfarin or NOACs with even minor head trauma should often have a CT and a period of observation."
  },
  {
    "Chief Complaint": "Chest / Abdominal Trauma / 가슴 외상 복부 외상",
    "Initial Action": "1. Primary Survey (ABCs): Assess for Tension Pneumothorax or Flail Chest.\n2. FAST Exam (Focused Assessment with Sonography for Trauma).\n3. Establish two large-bore IVs; initiate Massive Transfusion Protocol (MTP) if shock suspected.",
    "Red Flag Signs & Must-not-miss": "1. Tension Pneumothorax: Tracheal deviation, absent breath sounds, hypotension.\n2. Cardiac Tamponade: Beck’s Triad (Muffled heart sounds, JVD, hypotension).\n3. Massive Hemothorax: Hypotension + Dullness on percussion.\n4. Solid Organ Injury (Spleen/Liver laceration).\n5. Hollow Viscus Injury: Peritonitis signs.",
    "Common Causes (Top 5)": "1. Blunt Trauma (MVC, Fall).\n2. Penetrating Trauma (Stab, GSW).\n3. Blast Injuries.\n4. Crush Injuries.\n5. Deceleration Injuries (Aortic injury risk).",
    "Key History": "1. Mechanism: Seatbelt sign, steering wheel impact, or height of fall.\n2. Speed and position in vehicle.\n3. Presence of chest pain or abdominal pain.",
    "Physical Exam": "1. Chest: Look for ecchymosis, seatbelt sign, or subcutaneous emphysema.\n2. Abdomen: Check for guarding, distension, or Grey Turner/Cullen signs.\n3. Pelvis: Assess stability (Only once!).",
    "Tests & Purpose": "1. **FAST Exam:** Detect free fluid (blood) in pericardium, Morison’s pouch, splenorenal space, and pelvis.\n2. **Imaging Rules:** NEXUS/Canadian for C-spine.\n3. **X-ray Views:**\n   - **Chest:** Supine AP or Upright PA (Check for PTX/HTX/Widened mediastinum).\n   - **Pelvis:** AP view (Assess for fracture and potential source of hemorrhage).\n4. **CT Chest/Abdomen/Pelvis (with IV contrast):** For stable patients to identify organ injury or aortic dissection/rupture.",
    "Management": "1. Needle decompression / Tube thoracostomy for PTX/HTX.\n2. Hemostatic resuscitation (Blood products over crystalloids).\n3. Operative intervention (Laparotomy/Thoracotomy) for unstable bleeding.",
    "Consult & Disposition": "1. Trauma Surgery / General Surgery: Mandatory consult.\n2. Admission: For any significant organ injury or hemodynamic instability.",
    "Discharge & Warning": "1. Discharge only after negative imaging and a period of observation in minor blunt trauma.\n2. Warning: Return for worsening abdominal pain, dizziness, or SOB.",
    "Pearls & Pitfalls": "1. A 'negative' FAST does not rule out all intra-abdominal injuries (e.g., hollow viscus or retroperitoneal bleeds)."
  },
  {
    "Chief Complaint": "Laceration / Wound",
    "Initial Action": "1. Apply direct pressure to control hemorrhage.\n2. Assess distal neurovascular status *before* administering local anesthesia.\n3. Evaluate for 'Hard Signs' of vascular injury (e.g., pulsatile bleeding, expanding hematoma).",
    "Red Flag Signs & Must-not-miss": "1. Tendon or Nerve Laceration (Complete or partial).\n2. Open Joint / Penetrating Articular Injury.\n3. Foreign Body Retention (Glass, wood, metal).\n4. Compartment Syndrome (In crush/high-pressure injection injuries).\n5. Necrotizing Fasciitis (Pain out of proportion, crepitus).",
    "Common Causes (Top 5)": "1. Incised Wound (Knife, glass).\n2. Puncture Wound (Nail, needle).\n3. Abrasion / Road Rash.\n4. Laceration (Blunt trauma/tearing).\n5. Degloving Injury.",
    "Key History": "1. Mechanism of injury and time since occurrence (>6-12 hours increases infection risk).\n2. Tetanus immunization status.\n3. Presence of foreign body sensation.\n4. Comorbidities affecting healing (Diabetes, PVD, Immunosuppression).",
    "Physical Exam": "1. Assess 'Neurovascular Intactness': Pulse, capillary refill, 2-point discrimination, and motor function distal to the wound.\n2. Wound exploration: Visualize the base of the wound through full Range of Motion (ROM) to check for tendon/joint involvement.\n3. Check for 'Tendon Lag' or weakness against resistance.",
    "Tests & Purpose": "1. **X-ray Views (Soft Tissue Technique):** AP and Lateral of the affected area to detect radiopaque foreign bodies (metal, glass, some stones) or underlying fractures.\n2. **Ultrasound:** Useful for detecting radiolucent foreign bodies (wood, plastic) and assessing tendon integrity.",
    "Management": "1. Copious Irrigation: The most important step in preventing infection (Normal saline or tap water).\n2. Debridement: Remove devitalized tissue.\n3. Tetanus Prophylaxis: Tdap or Tetanus Immune Globulin (TIG) based on history.\n4. Closure: Primary (immediate), Delayed Primary (after 3-5 days), or Secondary Intention (healing on its own).",
    "Consult & Disposition": "1. Hand Surgery / Orthopedics: For complex tendon, nerve, or joint involvement.\n2. Plastic Surgery: For cosmetically sensitive areas (Face).\n3. Discharge: Most simple lacerations after repair.",
    "Discharge & Warning": "1. Wound care instructions (Keep clean/dry for 24-48h, suture removal timeline).\n2. Warning: Return for signs of infection (Increased redness, warmth, pus, or fever).",
    "Pearls & Pitfalls": "1. Never close a wound until you have explored it through the full range of motion to ensure no hidden tendon injury.\n2. 'Fight Bites' (Human bite over the MCP joint) should almost always be left open and treated with antibiotics."
  },
  {
    "Chief Complaint": "Burn 화상",
    "Initial Action": "1. Stop the burning process (Remove clothing, cool with room-temp water).\n2. Assess Airway: Look for signs of inhalation injury (Soot in oropharynx, singed nasal hairs).\n3. Establish IV access (preferably in non-burned skin) and start fluid resuscitation.",
    "Red Flag Signs & Must-not-miss": "1. Inhalation Injury: Risk of rapid airway edema.\n2. Circumferential Burns: Risk of Compartment Syndrome (requires escharotomy).\n3. Electrical Burns: Risk of internal injury and arrhythmias.\n4. Chemical Burns (especially Hydrofluoric Acid).\n5. Carbon Monoxide (CO) or Cyanide poisoning.",
    "Common Causes (Top 5)": "1. Scald (Hot liquids).\n2. Flame.\n3. Contact (Hot objects).\n4. Electrical.\n5. Chemical.",
    "Key History": "1. Environment: Closed space (Inhalation risk) vs. Open space.\n2. Burn source and duration of contact.\n3. Associated trauma (Explosions, falls).\n4. Baseline health (Renal/Cardiac status for fluid management).",
    "Physical Exam": "1. Calculate Total Body Surface Area (TBSA) using the **Rule of Nines** or Lund-Browder chart.\n2. Determine Burn Depth: 1st degree (erythema), 2nd degree (blisters/partial thickness), 3rd degree (leathery/full thickness).\n3. Distal pulse check in circumferential burns.",
    "Tests & Purpose": "1. **ABG / Carboxyhemoglobin:** Essential for suspected CO poisoning or inhalation injury.\n2. **EKG and CK:** For electrical burns to check for arrhythmias and rhabdomyolysis.\n3. **Chest X-ray:** Initial baseline; may be normal early in inhalation injury.",
    "Management": "1. Fluid Resuscitation: **Parkland Formula** (4 mL x kg x %TBSA) – Give half in first 8 hours.\n2. Pain Management: IV Opioids often required.\n3. Topical: Bacitracin or Silver Sulfadiazine (avoid Silver Sulfa on the face).",
    "Consult & Disposition": "1. Burn Center Referral: Criteria include >10% TBSA (partial thickness), burns to face/hands/feet/genitals, or 3rd-degree burns.\n2. Admission: For significant TBSA, inhalation injury, or inadequate pain control.",
    "Discharge & Warning": "1. Discharge for minor burns with daily dressing change instructions.\n2. Warning: Return for increased pain, fever, or spreading redness.",
    "Pearls & Pitfalls": "1. Do not use ice on burns; it causes vasoconstriction and worsens tissue ischemia.\n2. Inhalation injury may have a delayed presentation (up to 24h); have a low threshold for intubation."
  },
  {
    "Chief Complaint": "Animal / Insect Bite",
    "Initial Action": "1. Thoroughly irrigate the wound with high-pressure saline or soap/water.\n2. Assess for Anaphylaxis (Insect stings).\n3. Control bleeding and assess neurovascular status.",
    "Red Flag Signs & Must-not-miss": "1. Rabies Exposure (High-risk animals: Bats, raccoons, skunks).\n2. Systemic Envenomation (Venomous snakes/spiders): Coagulopathy, neurotoxicity.\n3. Pasteurella multocida Sepsis (Common in cat bites).\n4. Cat-Scratch Disease.\n5. Anaphylactic Shock.",
    "Common Causes (Top 5)": "1. Dog Bite (Most common).\n2. Cat Bite (Highest infection risk - puncture wounds).\n3. Human Bite (High infection risk - 'Fight bite').\n4. Bee / Wasp Stings.\n5. Snake / Spider Bites.",
    "Key History": "1. Animal type, health, and vaccination status.\n2. Time since bite.\n3. Patient's immune status (Splenectomy/Liver disease increases risk for Capnocytophaga).",
    "Physical Exam": "1. Inspect depth and involvement of joints/tendons.\n2. Look for signs of local infection (erythema, fluctuance).\n3. Check for lymphadenopathy.",
    "Tests & Purpose": "1. **X-ray Views:** To rule out retained teeth/foreign bodies or fractures.\n2. **Labs (Snake bite):** CBC, Coagulation panel (PT/INR, Fibrinogen), and CK to monitor for systemic venom effects.",
    "Management": "1. Antibiotics: **Amoxicillin-Clavulanate** is first-line for most mammalian bites.\n2. Rabies Post-exposure Prophylaxis (PEP): Vaccine + Human Rabies Immune Globulin (HRIG) if indicated.\n3. Tetanus prophylaxis.\n4. Antivenom: If systemic signs of snake/spider envenomation are present.",
    "Consult & Disposition": "1. Surgery: For deep wounds or those requiring debridement.\n2. Infectious Disease: For high-risk rabies or severe infections.\n3. Discharge: Most simple bites with antibiotics.",
    "Discharge & Warning": "1. Close follow-up (24-48h) to check for infection.\n2. Warning: Return for worsening pain, swelling, or red streaks (lymphangitis).",
    "Pearls & Pitfalls": "1. Cat bites often look minor but involve deep inoculation into tendons/joints; treat aggressively with antibiotics.\n2. Most bites should be left open or closed loosely; primary closure increases infection risk."
  },
  {
    "Chief Complaint": "Sore Throat",
    "Initial Action": "1. Assess Airway: Look for 'Tripod position', drooling, or stridor.\n2. Vital signs: Check for high fever and tachycardia.\n3. Keep NPO if airway obstruction or abscess is suspected.",
    "Red Flag Signs & Must-not-miss": "1. Epiglottitis: Rapid airway obstruction; 'Thumb sign' on X-ray.\n2. Peritonsillar Abscess (PTA): Trismus, uvular deviation.\n3. Retropharyngeal Abscess: Neck pain with extension, drooling.\n4. Lemierre Syndrome: Septic thrombophlebitis of the internal jugular vein.\n5. Ludwig’s Angina: Submandibular space infection; airway risk.",
    "Common Causes (Top 5)": "1. Viral Pharyngitis (Most common).\n2. Group A Strep Pharyngitis (GABHS).\n3. Infectious Mononucleosis (EBV).\n4. Tonsillitis.\n5. Peritonsillar Abscess.",
    "Key History": "1. Duration and severity of pain.\n2. Presence of 'Hot Potato Voice' or difficulty swallowing (Odynophagia).\n3. Recent history of dental work or URI.\n4. Presence of rash (Scarlet fever).",
    "Physical Exam": "1. Oral exam: Uvular deviation (PTA), tonsillar exudates, or pharyngeal erythema.\n2. External neck: Check for swelling, lymphadenopathy, and range of motion.\n3. Assess for 'Trismus' (inability to open mouth widely).",
    "Tests & Purpose": "1. **Rapid Strep / Throat Culture:** Use Centor Criteria to determine need.\n2. **Monospot Test:** For suspected Mononucleosis.\n3. **Lateral Neck X-ray:** To visualize the epiglottis ('Thumb sign') and prevertebral space.\n4. **CT Neck (with Contrast):** Gold standard for diagnosing PTA or Retropharyngeal abscess.",
    "Management": "1. Antibiotics: Penicillin or Amoxicillin for GABHS.\n2. Steroids (Dexamethasone): To reduce swelling in PTA or severe Mono.\n3. Needle Aspiration / I&D: For Peritonsillar abscess.",
    "Consult & Disposition": "1. ENT: For abscess drainage or suspected epiglottitis.\n2. Admission: For airway compromise, inability to tolerate PO, or deep space infection.",
    "Discharge & Warning": "1. Discharge simple pharyngitis with follow-up.\n2. Warning: Return for difficulty breathing, inability to swallow saliva, or muffled voice.",
    "Pearls & Pitfalls": "1. Avoid examining the throat with a tongue depressor if epiglottitis is suspected; it may trigger laryngospasm.\n2. Mononucleosis patients should avoid contact sports (risk of splenic rupture)."
  },
  {
    "Chief Complaint": "Epistaxis / 코피",
    "Initial Action": "1. Have the patient lean forward and apply constant pressure to the alae for 10-15 minutes.\n2. Assess Hemodynamics: Check HR and BP.\n3. Clear the nose of clots with suction or by blowing.",
    "Red Flag Signs & Must-not-miss": "1. Posterior Epistaxis: Bleeding that cannot be visualized or controlled by anterior pressure.\n2. Airway Compromise / Aspiration.\n3. Hemorrhagic Shock.\n4. Coagulopathy: Uncontrolled bleeding due to anticoagulants or blood disorders.",
    "Common Causes (Top 5)": "1. Digital Trauma (Nose picking).\n2. Dry Air / Low humidity.\n3. Anticoagulant / Antiplatelet use.\n4. Recent URI / Allergies.\n5. Foreign Body (especially in children).",
    "Key History": "1. Duration, frequency, and severity.\n2. Use of anticoagulants (Warfarin, NOACs) or Aspirin.\n3. History of trauma or intranasal drug use (Cocaine).\n4. Family history of bleeding disorders (e.g., HHT).",
    "Physical Exam": "1. Identify the source: Anterior (Kiesselbach’s plexus) vs. Posterior.\n2. Check the oropharynx for active bleeding down the back of the throat.\n3. Monitor vitals for hypotension/tachycardia.",
    "Tests & Purpose": "1. **CBC / Coagulation Panel:** If bleeding is severe, recurrent, or patient is on anticoagulants.\n2. **Type & Screen:** For massive epistaxis.\n3. **X-ray Views:** Only if significant midface trauma is suspected.",
    "Management": "1. Topical Vasoconstrictors: Oxymetazoline (Afrin) or Phenylephrine.\n2. Chemical Cautery: Silver Nitrate (only if the vessel is seen and bleeding is slow).\n3. Anterior Packing: Nasal tampons (Rhino Rocket) or ribbon gauze.\n4. Posterior Packing: Balloon catheters (Foley or Epistat).",
    "Consult & Disposition": "1. ENT: For posterior bleeds or those requiring surgical ligation/embolization.\n2. Admission: Mandatory for posterior packing (due to risk of hypoxia/arrhythmia).",
    "Discharge & Warning": "1. Discharge anterior bleeds with packing in place for 48-72h.\n2. Warning: Return for persistent bleeding through the pack or if it falls out.",
    "Pearls & Pitfalls": "1. Do not use cautery on both sides of the septum (risk of perforation).\n2. Hypertensive patients with epistaxis: Treat the bleeding first; BP often drops once the bleeding and anxiety are controlled."
  },
  {
    "Chief Complaint": "Eye Pain / Vision Loss",
    "Initial Action": "1. Check Visual Acuity (The 'Vitals' of the eye) – use Snellen chart or near card.\n2. Chemical Exposure? Immediate irrigation with 2-3L of saline until pH is 7.0–7.2 (Check before and after).\n3. Shield the eye if Globe Rupture is suspected; do not apply pressure or measure IOP.",
    "Red Flag Signs & Must-not-miss": "1. Central Retinal Artery Occlusion (CRAO): Sudden, painless vision loss ('Cherry red spot').\n2. Acute Angle-Closure Glaucoma (AACG): Pain, 'halos', mid-dilated fixed pupil, high IOP.\n3. Retinal Detachment: 'Curtain' over vision, flashes, and floaters.\n4. Orbital Compartment Syndrome (OCS): Proptosis + Decreased vision (requires lateral canthotomy).\n5. Endophthalmitis: Deep pain/redness after recent eye surgery.",
    "Common Causes (Top 5)": "1. Corneal Abrasion / Foreign Body.\n2. Conjunctivitis (Bacterial/Viral).\n3. Iritis / Uveitis.\n4. Keratitis (especially HSV).\n5. Vitreous Hemorrhage.",
    "Key History": "1. Onset: Sudden vs. Gradual.\n2. Pain: Painful (Cornea/Glaucoma) vs. Painless (CRAO/Detachment).\n3. Trauma 기전: High-speed metal-on-metal (risk of intraocular foreign body).\n4. Contacts: Prolonged wear (risk of Pseudomonas keratitis).",
    "Physical Exam": "1. Pupillary Response: Assess for Relative Afferent Pupillary Deficit (RAPD).\n2. Slit Lamp: Check for cells/flare (Uveitis), hypopyon, or dendritic lesions (HSV).\n3. Tonometry: Measure Intraocular Pressure (IOP) – Normal is 10–21 mmHg.",
    "Tests & Purpose": "1. **Fluorescein Staining:** Identify abrasions, ulcers, or Seidel’s sign (Globe rupture).\n2. **CT Maxillofacial / Orbit:** For trauma; assess for Blowout fracture or foreign body.\n3. **X-ray Views:** Waters' view (Old-school for orbit) – CT is now gold standard.",
    "Management": "1. AACG: Timolol drops, Acetazolamide, and IV Mannitol.\n2. CRAO: Ocular massage, call Ophthalmology immediately.\n3. Abrasion: Topical antibiotics (Erythromycin or Ciprofloxacin for contact users).",
    "Consult & Disposition": "1. Ophthalmology: Immediate for CRAO, AACG, Globe rupture, or OCS.\n2. Admission: For Endophthalmitis or severe Orbital Cellulitis.",
    "Discharge & Warning": "1. Discharge abrasions with 24h follow-up.\n2. Warning: Return for worsening pain or further vision loss. **Never** prescribe topical anesthetics for home use.",
    "Pearls & Pitfalls": "1. A normal-looking eye with sudden, painless vision loss is a vascular emergency until proven otherwise.\n2. Always check pH in chemical burns *before* anything else."
  },
  {
    "Chief Complaint": "Red Eye",
    "Initial Action": "1. Assess Visual Acuity – a red eye with normal vision is usually less urgent.\n2. Rule out trauma or chemical exposure.\n3. Implement infection control if viral conjunctivitis is suspected.",
    "Red Flag Signs & Must-not-miss": "1. Ciliary Flush: Redness most intense at the limbus (sign of Glaucoma, Uveitis, or Keratitis).\n2. Corneal Ulcer: White infiltrate on the cornea.\n3. Scleritis: Severe 'boring' pain, violet hue; associated with systemic AI disease.\n4. Orbital Cellulitis: Fever, proptosis, and painful eye movements.\n5. Hypopyon: Layer of pus in the anterior chamber.",
    "Common Causes (Top 5)": "1. Conjunctivitis (Viral/Bacterial/Allergic).\n2. Subconjunctival Hemorrhage (Asymptomatic, 'bloody' appearance).\n3. Corneal Abrasion.\n4. Blepharitis / Chalazion.\n5. Episcleritis.",
    "Key History": "1. Discharge: Purulent (Bacterial) vs. Watery (Viral) vs. Mucoid/Itchy (Allergic).\n2. Photophobia (Suggests Iritis or Keratitis).\n3. Contact lens use.\n4. Associated systemic symptoms (Joint pain, rashes).",
    "Physical Exam": "1. Pattern of redness (Diffuse vs. Localized vs. Ciliary flush).\n2. Eversion of eyelids to check for foreign bodies.\n3. Check for lymphadenopathy (Preauricular nodes in viral conjunctivitis).",
    "Tests & Purpose": "1. **Slit Lamp Exam:** Evaluate cornea and anterior chamber.\n2. **Fluorescein Stain:** Look for Seidel sign or dendritic patterns.",
    "Management": "1. Bacterial: Topical antibiotics (Polytrim or Fluoroquinolones).\n2. Viral: Supportive, artificial tears, cool compresses.\n3. Subconjunctival Hemorrhage: Reassurance (resolves in 1–2 weeks).",
    "Consult & Disposition": "1. Ophthalmology: For Uveitis, Scleritis, or Keratitis.\n2. Discharge: Most simple conjunctivitis cases.",
    "Discharge & Warning": "1. Warning: Return for vision changes, severe pain, or if no improvement in 48h.\n2. Education: Hand hygiene for viral cases.",
    "Pearls & Pitfalls": "1. Subconjunctival hemorrhage is the 'bruise' of the eye—it looks scary to the patient but is usually benign unless trauma-related."
  },
  {
    "Chief Complaint": "Ear Pain / Hearing Loss",
    "Initial Action": "1. Perform Otoscopy to visualize the TM and canal.\n2. Assess for Mastoid tenderness or post-auricular erythema.\n3. Screen for facial nerve palsy.",
    "Red Flag Signs & Must-not-miss": "1. Necrotizing (Malignant) Otitis Externa: Invasive infection in elderly/diabetics; cranial nerve involvement.\n2. Sudden Sensorineural Hearing Loss (SSHL): Emergency; requires prompt steroids.\n3. Mastoiditis: Displaced pinna, retroauricular swelling.\n4. Temporal Bone Fracture: Hemotympanum or Battle’s sign.\n5. Ramsay Hunt Syndrome: Herpes Zoster Oticus; vesicles in canal + facial palsy.",
    "Common Causes (Top 5)": "1. Otitis Externa (Swimmer's ear).\n2. Acute Otitis Media (AOM).\n3. Cerumen Impaction.\n4. Eustachian Tube Dysfunction (ETD).\n5. Bullous Myringitis.",
    "Key History": "1. Onset of hearing loss: Sudden (minutes/hours) vs. Gradual.\n2. Trauma 기전: Q-tip use, diving, or direct blow to head.\n3. History of Diabetes or Immunosuppression (Risk for Malignant OE).\n4. Associated vertigo or tinnitus.",
    "Physical Exam": "1. Tug Test: Pain with traction of the pinna (Otitis Externa).\n2. Weber and Rinne Tests: Differentiate Conductive vs. Sensorineural loss.\n3. CN VII Exam: Check for facial symmetry.",
    "Tests & Purpose": "1. **CT Temporal Bone:** For suspected Mastoiditis, Malignant OE, or Trauma.\n2. **X-ray Views:** Schüller’s view (Historically for mastoid) – CT is preferred now.",
    "Management": "1. Otitis Externa: Cipro/Dexa otic drops.\n2. AOM: Amoxicillin (if indicated by AAP/AAO guidelines).\n3. SSHL: High-dose oral Prednisone and urgent ENT follow-up.",
    "Consult & Disposition": "1. ENT: For SSHL, Mastoiditis, or Malignant OE.\n2. Admission: For IV antibiotics (Mastoiditis/Malignant OE).",
    "Discharge & Warning": "1. Discharge simple OE/AOM with outpatient follow-up.\n2. Warning: Return for facial weakness, severe headache, or confusion.",
    "Pearls & Pitfalls": "1. Any 'Otitis Externa' in a diabetic patient that does not respond to drops must be evaluated for Malignant OE."
  },
  {
    "Chief Complaint": "Dental Pain / 치통",
    "Initial Action": "1. Assess Airway: Check for floor-of-mouth swelling or 'Hot potato' voice.\n2. Vital signs: Check for fever/tachycardia.\n3. Provide analgesia (NSAIDs are often superior to opioids).",
    "Red Flag Signs & Must-not-miss": "1. Ludwig’s Angina: Rapidly spreading cellulitis of the submandibular space; airway emergency.\n2. Cavernous Sinus Thrombosis: Fever, proptosis, and CN palsies from dental spread.\n3. Deep Space Infection: Trismus (inability to open mouth), drooling.\n4. Atypical MI: Referred pain to the jaw (especially in elderly).",
    "Common Causes (Top 5)": "1. Dental Caries / Pulpitis.\n2. Periapical Abscess.\n3. Pericoronitis (Infection around third molars/wisdom teeth).\n4. Alveolar Osteitis ('Dry Socket' – post-extraction).\n5. Periodontal Abscess.",
    "Key History": "1. Pain triggers: Hot vs. Cold (Pulpitis).\n2. Recent dental procedures (Dry socket usually 3–5 days post-op).\n3. Systemic symptoms (Fever, chills).\n4. Immunosuppression.",
    "Physical Exam": "1. Intraoral: Percuss teeth for tenderness; check for fluctuant masses.\n2. Extraoral: Assess for facial symmetry and submandibular fullness.\n3. Assess 'Trismus': Gap <3 fingers is concerning.",
    "Tests & Purpose": "1. **CT Neck (with Contrast):** Gold standard for deep space infections/abscess.\n2. **Panorex:** Detailed view of teeth and mandible (rarely available in ER; usually plain films or CT).",
    "Management": "1. Nerve Block: Inferior alveolar or supraperiosteal block for immediate relief.\n2. Antibiotics: Penicillin VK, Amoxicillin, or Clindamycin.\n3. Dry Socket: Pack with eugenol (clove oil) gauze.",
    "Consult & Disposition": "1. OMFS (Oral-Maxillofacial Surgery) / ENT: For deep space infections or I&D.\n2. Discharge: Most simple dental pain to follow up with a dentist within 24–48h.",
    "Discharge & Warning": "1. Warning: Return for difficulty breathing, difficulty swallowing, or spreading facial swelling.",
    "Pearls & Pitfalls": "1. If a patient has 'dental pain' but a normal oral exam, think of Sinusitis or Myocardial Ischemia."
  },
  {
    "Chief Complaint": "Poor Feeding (소아)",
    "Initial Action": "1. **Pediatric Assessment Triangle (PAT):** Assess Appearance, Work of Breathing, and Circulation.\n2. Bedside Glucose (BST): Rule out hypoglycemia.\n3. Accurate weight and check for dehydration (Weight loss from birth/baseline).",
    "Red Flag Signs & Must-not-miss": "1. Sepsis: In neonates (<28 days), poor feeding may be the *only* sign.\n2. Congenital Heart Disease (CHD): Feeding difficulty with diaphoresis and tachypnea.\n3. Inborn Errors of Metabolism (IEM): Lethargy, vomiting, odd smell.\n4. Intussusception: Periodic fussiness/crying.\n5. Non-accidental Trauma (Child Abuse).",
    "Common Causes (Top 5)": "1. Viral Illness (URI/Gastroenteritis).\n2. Poor Feeding Technique (Latching/positioning).\n3. Stomatitis / Oral Thrush.\n4. Urinary Tract Infection (Occult source).\n5. Constipation / Colic.",
    "Key History": "1. Hydration: Number of wet diapers (<4 in 24h is concerning).\n2. Vomiting: Bilious (Emergency) vs. Non-bilious.\n3. Birth history: Prematurity, maternal GBS status.\n4. Feeding behavior: Sweating or tiring during feeds (Cardiac).",
    "Physical Exam": "1. General: Assess tone and level of alertness.\n2. Fontanelle: Sunken (dehydration) vs. Bulging (increased ICP).\n3. Heart: Check for murmurs and hepatomegaly.\n4. Abdomen: Palpate for 'sausage-shaped' mass (Intussusception).",
    "Tests & Purpose": "1. **Full Sepsis Workup:** (CBC, Blood/Urine/CSF cultures) for febrile/ill neonates.\n2. **CXR:** Look for cardiomegaly or pulmonary edema.\n3. **Electrolytes/BUN/Cr:** Assess for pyloric stenosis (hypochloremic alkalosis) or dehydration.",
    "Management": "1. Rehydration: IV Bolus (Normal Saline 20 mL/kg) or trial of PO/pedialyte.\n2. Glucose correction if needed.\n3. Empirical antibiotics if sepsis is suspected.",
    "Consult & Disposition": "1. Pediatrics: For most poor feeders with no clear benign cause.\n2. Admission: For failure to thrive, severe dehydration, or sepsis workup.",
    "Discharge & Warning": "1. Discharge only if PAT is reassuring, hydration is adequate, and close follow-up is secured.\n2. Warning: Return for lethargy, bile-stained vomiting, or fever.",
    "Pearls & Pitfalls": "1. A neonate who is 'too tired to eat' is a neonate who is in shock until proven otherwise."
  },
  {
    "Chief Complaint": "Lethargy / Irritability (소아)",
    "Initial Action": "1. **Pediatric Assessment Triangle (PAT):** Immediate assessment of Appearance (Tone, Interactiveness, Consolability, Gaze, Speech/Cry).\n2. **Bedside Glucose (BST):** Rule out hypoglycemia (especially in neonates).\n3. Check vitals and obtain a core temperature (Rectal for infants).",
    "Red Flag Signs & Must-not-miss": "1. Meningitis / Encephalitis: Bulging fontanelle, nuchal rigidity (may be absent in infants), non-blanching rash.\n2. Inborn Errors of Metabolism (IEM): Metabolic acidosis, hyperammonemia.\n3. Intussusception: Periodic irritability followed by lethargy ('lethargy' can be the primary symptom).\n4. Non-Accidental Trauma (NAT): Shaken Baby Syndrome (Look for retinal hemorrhages, bulging fontanelle).\n5. Sepsis: Inconsolable crying or paradoxical irritability (crying more when held).",
    "Common Causes (Top 5)": "1. Viral Infection (Early systemic phase).\n2. Dehydration (e.g., from Gastroenteritis).\n3. Urinary Tract Infection (Occult sepsis source).\n4. Otitis Media / Pharyngitis (Pain causing irritability).\n5. Colic / Constipation.",
    "Key History": "1. Definition of 'Lethargy': Does the child track with their eyes? Do they wake up to painful stimuli? (True lethargy is a medical emergency).\n2. Feeding/Voiding history (Hydration status).\n3. Trauma history (Falls, 'accidental' injuries).\n4. Toxic exposures (Access to medications at home).",
    "Physical Exam": "1. **Undressed Exam:** Strip the child completely to check for 'Hair Tourniquets' (toes/fingers/penis), occult bruises, or rashes.\n2. Neurological: Level of consciousness, muscle tone, and fontanelle assessment.\n3. Abdominal: Palpate for masses or tenderness.",
    "Tests & Purpose": "1. **Sepsis Workup:** CBC, CRP, Blood/Urine/CSF cultures (if criteria met).\n2. **Electrolytes & Ammonia:** Rule out hyponatremia or IEM.\n3. **Imaging:** \n   - **Head CT:** If NAT or intracranial pathology is suspected.\n   - **Abdominal Ultrasound:** If intussusception is suspected.",
    "Management": "1. Airway/Breathing support as needed.\n2. IV/IO fluid bolus (20 mL/kg NS) if shock/dehydration suspected.\n3. Empirical antibiotics and acyclovir if CNS infection is suspected.",
    "Consult & Disposition": "1. Pediatrics: Mandatory for any child with true lethargy or unexplained irritability.\n2. Admission: Most cases require a period of observation or a full workup.",
    "Discharge & Warning": "1. Discharge only if a benign cause is found and the child is back to their baseline mental status.\n2. Warning: Return for persistent lethargy, seizure, or if the child becomes 'impossible to wake up'.",
    "Pearls & Pitfalls": "1. **Pitfall:** Labeling a lethargic child as 'just sleepy.' If they don't wake up for a blood draw, they are lethargic.\n2. **Pearl:** In infants, 'paradoxical irritability' (crying more when being comforted/held) is a classic sign of meningeal irritation."
  },
  {
    "Chief Complaint": "Pediatric Fever 소아",
    "Initial Action": "1. Triage by Age: <28 days, 29-60 days, and 61-90 days have different management algorithms.\n2. Assess PAT and vitals; focus on 'Work of Breathing' and 'Circulation to Skin'.\n3. Provide antipyretics if the child is uncomfortable (Acetaminophen 15mg/kg).",
    "Red Flag Signs & Must-not-miss": "1. Neonatal Fever (<28 days): High risk for Serious Bacterial Infection (SBI).\n2. Toxic Appearance: Pale/mottled skin, weak cry, poor perfusion.\n3. Petechial or Purpuric Rash: Suggests Meningococcemia.\n4. Incomplete Immunization: Increases risk for Strep. pneumoniae or H. influenzae sepsis.",
    "Common Causes (Top 5)": "1. Viral Upper Respiratory Infection (URI).\n2. Acute Otitis Media (AOM).\n3. Urinary Tract Infection (UTI) - Most common SBI in girls and uncircumcised boys.\n4. Viral Exanthems (Roseola, etc.).\n5. Viral Gastroenteritis.",
    "Key History": "1. Exact age (in days/weeks).\n2. Highest temperature and duration of fever.\n3. Behavior: Is the child playful when the fever drops? (Reassuring sign).\n4. Ill contacts and immunization history.",
    "Physical Exam": "1. Focus on finding a source: Ears, throat, lungs, abdomen.\n2. Skin: Check for any rashes or signs of soft tissue infection.\n3. Hydration: Mucous membranes, fontanelle, and capillary refill.",
    "Tests & Purpose": "1. **Full Sepsis Workup (<28 days):** CBC, Blood Culture, UA/UC, and LP (MANDATORY).\n2. **Step-by-Step / PECARN Criteria (29-60/90 days):** To determine the need for LP based on inflammatory markers (Procalcitonin, CRP, ANC).\n3. **UA/UC:** Should be obtained in all girls <24 months and uncircumcised boys <12 months with FUO.",
    "Management": "1. Fever control (Acetaminophen/Ibuprofen - avoid Ibuprofen in <6 months).\n2. Rehydration (PO or IV).\n3. **Antibiotics:** Ampicillin + Gentamicin/Cefotaxime for neonates.",
    "Consult & Disposition": "1. Pediatrics: For all febrile neonates or toxic-appearing children.\n2. Admission: Mandatory for <28 days; 29-60 days based on risk-stratification.",
    "Discharge & Warning": "1. Discharge if low-risk criteria are met and follow-up is guaranteed in 24h.\n2. Warning: Return for decreased activity, poor feeding, or if a new rash develops.",
    "Pearls & Pitfalls": "1. **Pearl:** Response to 해열제 (Antipyretics) does **not** differentiate between viral and bacterial infections.\n2. **Pitfall:** Forgetting to check a urine sample in a febrile infant with no clear source."
  },
  {
    "Chief Complaint": "Pediatric Seizure 소아",
    "Initial Action": "1. Airway: Suctioning, positioning (lateral), and O2 if needed.\n2. **Active Seizure (>5 min):** Midazolam (IM/IN) or Lorazepam (IV).\n3. **Bedside Glucose (BST):** Check immediately during or after the event.",
    "Red Flag Signs & Must-not-miss": "1. Complex Febrile Seizure: Duration >15 min, focal features, or recurrences within 24h.\n2. Meningitis / Encephalitis: Fever + Seizure + Prolonged post-ictal phase.\n3. Intracranial Hemorrhage: Trauma or NAT (Shaken Baby).\n4. Hyponatremia: From improper formula dilution or excessive water intake.",
    "Common Causes (Top 5)": "1. Simple Febrile Seizure (6 months - 5 years).\n2. Epilepsy (Known or New-onset).\n3. Viral Illness with High Fever.\n4. Hypoglycemia.\n5. Hyponatremic Seizure (Infants).",
    "Key History": "1. Seizure character: Generalized tonic-clonic vs. Focal.\n2. Duration and 'Last Known Normal'.\n3. Post-ictal phase: How long did it take to return to baseline? (Should be <30 min for simple febrile).\n4. Family history of seizures and recent trauma.",
    "Physical Exam": "1. Neurological: Check for focal deficits (Todd's paralysis) and mental status.\n2. Skin: Look for Neurofibromatosis/TSC signs or bruising (NAT).\n3. Head circumference and fontanelle in infants.",
    "Tests & Purpose": "1. **BST & Electrolytes:** Especially Na+ in infants <6 months.\n2. **Lumbar Puncture (LP):** If meningitis is suspected or in infants <6-12 months with questionable immunization.\n3. **Imaging (CT Head):** For first-time non-febrile seizure, focal onset, or trauma.\n4. **AED Levels:** If the child is on chronic seizure medications.",
    "Management": "1. Benzodiazepines for status epilepticus.\n2. Antipyretics if febrile.\n3. Standardized loading doses (Fosphenytoin/Levetiracetam) for refractory cases.",
    "Consult & Disposition": "1. Pediatric Neurology: For new-onset non-febrile seizures.\n2. Admission: For status epilepticus, complex febrile seizures requiring workup, or suspected infection.",
    "Discharge & Warning": "1. Discharge simple febrile seizures after return to baseline and parental education.\n2. Warning: Return if seizure lasts >5 min, child does not wake up, or focal weakness occurs.",
    "Pearls & Pitfalls": "1. **Pearl:** Simple febrile seizures are benign and do **not** require extensive workup or neuroimaging.\n2. **Pitfall:** Missing an intracranial bleed in an infant who 'fell' but now has a seizure."
  },
  {
    "Chief Complaint": "Pediatric Respiratory Distress 소아",
    "Initial Action": "1. **PAT:** Assess 'Work of Breathing' (Retractions, Grunting, Flaring) and 'Appearance'.\n2. Provide O2 (blow-by or mask) as tolerated; avoid agitating the child.\n3. Position of Comfort: Allow the child to stay in the parent's lap.",
    "Red Flag Signs & Must-not-miss": "1. Epiglottitis: Stridor, drooling, tripod position (Medical emergency).\n2. Foreign Body Aspiration (FBA): Sudden onset of choking/coughing, focal wheezing.\n3. Bacterial Tracheitis: Toxic appearance + Stridor.\n4. Status Asthmaticus: 'Silent chest' (No air movement).\n5. Congenital Heart Disease: Respiratory distress with hepatomegaly/cyanosis.",
    "Common Causes (Top 5)": "1. Croup (Laryngotracheobronchitis).\n2. Bronchiolitis (RSV).\n3. Asthma Exacerbation.\n4. Pneumonia.\n5. Viral Upper Respiratory Infection.",
    "Key History": "1. Onset: Sudden (FBA) vs. Gradual (Infection).\n2. Cough: Barking (Croup) vs. Productive (Pneumonia).\n3. Fever, ill contacts, and history of prematurity/asthma.\n4. Choking episode while eating or playing.",
    "Physical Exam": "1. Auscultation: Stridor (Inspiratory = Upper airway) vs. Wheezing (Expiratory = Lower airway).\n2. Retractions: Subcostal, intercostal, suprasternal.\n3. Check for cyanosis or clubbing.",
    "Tests & Purpose": "1. **CXR:** AP and Lateral (Check for infiltrates, hyperinflation, or FBA).\n2. **Lateral Neck X-ray:** 'Thumb sign' (Epiglottitis) or 'Steeple sign' (Croup).\n3. **Viral PCR:** To confirm RSV/Flu/COVID.",
    "Management": "1. Croup: Nebulized Epinephrine and Dexamethasone (0.6 mg/kg).\n2. Asthma/Bronchiolitis: Albuterol nebs (if indicated) and nasal suctioning.\n3. HFNC (High-Flow Nasal Cannula) for moderate-to-severe distress.",
    "Consult & Disposition": "1. Pediatrics / PICU: For respiratory failure or required NIV.\n2. Admission: For supplemental O2 requirement, poor feeding, or severe retractions.",
    "Discharge & Warning": "1. Discharge if O2 sat is stable (>92-94%), retractions are mild, and child is hydrated.\n2. Warning: Return for 'caving in' of the chest, blue lips, or inability to drink fluids.",
    "Pearls & Pitfalls": "1. **Pearl:** A child with croup who has stridor **at rest** requires nebulized epinephrine and observation for at least 3-4 hours.\n2. **Pitfall:** Agitating a child with suspected epiglottitis (e.g., trying to look at the throat) can cause total airway collapse."
  },
  {
    "Chief Complaint": "Pediatric Crying / Inconsolable 소아",
    "Initial Action": "1. **Undressed Exam:** Strip the child naked to find a source of pain.\n2. Check vitals (especially temperature).\n3. Assess for PAT (Is the child 'toxic'?).",
    "Red Flag Signs & Must-not-miss": "1. Intussusception: Periodic episodes of intense crying with 'sausage' mass.\n2. Testicular Torsion / Incarcerated Hernia: Must check the diaper area.\n3. Hair Tourniquet: Check fingers, toes, and penis.\n4. Corneal Abrasion: Use fluorescein if no other source is found.\n5. NAT (Abuse): Rib fractures or long bone fractures.",
    "Common Causes (Top 5)": "1. Infantile Colic (Diagnosis of exclusion).\n2. Otitis Media.\n3. Urinary Tract Infection.\n4. Constipation / Anal Fissure.\n5. Diaper Dermatitis.",
    "Key History": "1. Duration and pattern (Periodic vs. Constant).\n2. Feeding and stooling (Currant jelly stool? blood?).\n3. Any recent falls or trauma.\n4. Caregiver stress level (Assess risk for abuse).",
    "Physical Exam": "1. **Head-to-Toe:** Check ears (AOM), eyes (Fluorescein), mouth (Thrush), and joints (Septic arthritis).\n2. **Genitourinary:** Incarcerated hernia or torsion.\n3. **Skin:** Bruising, tourniquets, or signs of burns.",
    "Tests & Purpose": "1. **Fluorescein Stain:** Identify corneal abrasion.\n2. **Abdominal Ultrasound:** If intussusception is suspected (periodic crying).\n3. **UA/UC:** Rule out UTI.\n4. **X-ray (Skeletal survey):** If abuse is suspected.",
    "Management": "1. Treat the underlying cause (e.g., Sucrose for pain, antibiotics for infection).\n2. Reassurance and education for colic.\n3. Reduction of hernia or intussusception.",
    "Consult & Disposition": "1. Surgery: For torsion, intussusception, or incarcerated hernia.\n2. Discharge: Most cases where a benign or no source is found, provided the child is stable.",
    "Discharge & Warning": "1. Education on 'Purple Crying' and Shaken Baby prevention.\n2. Warning: Return for bile-stained vomiting, blood in stool, or fever.",
    "Pearls & Pitfalls": "1. **Pearl:** If a child stops crying when you still them, think of a fracture or septic arthritis (pain with movement).\n2. **Pitfall:** Forgetting to check the diaper area in a crying baby."
  },
  {
    "Chief Complaint": "Foreign Body (Airway, Eye, Ear, Nose, Rectum)",
    "Initial Action": "1. Airway: Assess for stridor or complete obstruction (Heimlich maneuver / Back blows).\n2. Ocular/Chemical: Immediate irrigation if caustic; check visual acuity.\n3. Identify the object: **Button Batteries** are a surgical emergency in the esophagus, nose, or ear.",
    "Red Flag Signs & Must-not-miss": "1. Button Battery: Causes liquefactive necrosis within 2 hours.\n2. Airway Obstruction: Sudden coughing, wheezing, or cyanosis.\n3. Multiple Magnets (Ingested): Risk of bowel entrapment and perforation.\n4. Penetrating Eye Injury: Seidel's sign, peaked pupil.\n5. Sharp Objects in Esophagus: High risk of perforation.",
    "Common Causes (Top 5)": "1. Ingested Coins (Pediatrics).\n2. Food Bolus (Adults/Elderly).\n3. Inhaled Organic Matter (Peanuts/Popcorn).\n4. Nasal/Aural Beads or Batteries.\n5. Retained Rectal/Vaginal objects.",
    "Key History": "1. Type of object (Metal, organic, battery, sharp).\n2. Timing of incident and onset of symptoms (e.g., choking episode).\n3. Associated pain, bleeding, or difficulty breathing.",
    "Physical Exam": "1. Airway: Listen for focal wheezing or stridor.\n2. ENT: Direct visualization with otoscope/rhinoscope.\n3. Rectal: Palpate for orientation and sharpness before removal attempt.",
    "Tests & Purpose": "1. **X-ray Views:**\n   - **Neck/Chest/Abdomen:** AP and Lateral (Check for 'Double-contour sign' in batteries).\n   - **Inspiratory/Expiratory Chest X-ray:** Check for air trapping in airway foreign bodies.\n2. **CT Scan:** For non-radiopaque objects (e.g., wood, plastic) or suspected perforation.",
    "Management": "1. Airway/Esophageal: Urgent Endoscopy or Bronchoscopy.\n2. Nasal/Aural: Specialized tools (Katz extractor, alligator forceps); **do not** irrigate organic matter (it swells).\n3. Rectal: Manual removal or surgical consult if high/sharp.",
    "Consult & Disposition": "1. GI/ENT/Pulmonology: Based on location for extraction.\n2. Admission: For any battery ingestion in the esophagus or signs of perforation.",
    "Discharge & Warning": "1. Discharge after successful removal and observation for trauma.\n2. Warning: Return for fever, abdominal pain, or bloody stools/vomit.",
    "Pearls & Pitfalls": "1. **Pearl:** A coin in the esophagus shows its 'face' on AP X-ray, while a coin in the trachea shows its 'edge'.\n2. **Pitfall:** Delaying removal of a button battery in the nose or ear; it can cause septal perforation or hearing loss very quickly."
  },
  {
    "Chief Complaint": "Heat / Cold Injury",
    "Initial Action": "1. Secure ABCs and monitor core temperature (Rectal probe is mandatory).\n2. Move to a controlled environment (Cooling vs. Rewarming).\n3. Assess mental status (Heatstroke vs. Exhaustion).",
    "Red Flag Signs & Must-not-miss": "1. Heatstroke: Core temp >40°C + Altered Mental Status (Medical emergency).\n2. Severe Hypothermia (<28°C): Risk of 'Osborn J waves' and V-fib.\n3. Rhabdomyolysis / Acute Renal Failure.\n4. Frostbite: Risk of permanent tissue loss.\n5. Paradoxical Undressing: Sign of severe hypothermia.",
    "Common Causes (Top 5)": "1. Heat Exhaustion (Dehydration + hyperthermia).\n2. Heatstroke (Classic vs. Exertional).\n3. Accidental Hypothermia (Environmental exposure).\n4. Frostbite (Peripheral cold injury).\n5. Heat Edema / Cramps.",
    "Key History": "1. Duration of exposure and ambient temperature.\n2. Activity level (Exertional heatstroke common in athletes/military).\n3. Alcohol or drug use (Common in hypothermia).\n4. Comorbidities (Elderly, infants, or thyroid disease).",
    "Physical Exam": "1. Mental status: Confusion, seizure, or coma.\n2. Skin: Sweating (Exhaustion) vs. Anhidrosis (Late heatstroke); Skin color/sensation (Frostbite).\n3. Vitals: Tachycardia, hypotension, and rectal temp.",
    "Tests & Purpose": "1. **Electrolytes & Renal Panel:** Check for Na+ imbalance and AKI.\n2. **CK / Myoglobin:** Assess for Rhabdomyolysis.\n3. **ECG:** Check for Osborn waves (Hypothermia) or ischemia (Heatstroke).\n4. **Imaging:** X-ray only if trauma suspected during fall/collapse.",
    "Management": "1. Heat: Evaporative cooling (Mist + Fan), ice-water immersion (Exertional), and IV fluids.\n2. Cold: Passive rewarming (blankets) vs. Active internal rewarming (warmed IV fluids, gastric/peritoneal lavage).\n3. Frostbite: Rapid rewarming in 37-39°C water bath.",
    "Consult & Disposition": "1. ICU: For heatstroke or severe hypothermia.\n2. Nephrology: For dialysis if severe rhabdomyolysis/AKI.\n3. Burn Center: For severe frostbite.",
    "Discharge & Warning": "1. Discharge if cause resolved, labs normal, and patient is stable.\n2. Warning: Avoid re-exposure; follow up for skin changes in frostbite.",
    "Pearls & Pitfalls": "1. **Pearl:** In hypothermia, 'You are not dead until you are warm and dead.'\n2. **Pitfall:** Misdiagnosing heatstroke as simple dehydration; the key differentiator is the CNS status."
  },
  {
    "Chief Complaint": "Electrical Injury",
    "Initial Action": "1. Ensure the patient is disconnected from the power source safely.\n2. ABCs and immediate Cardiac Monitoring.\n3. Immobilize C-spine (High risk of falls or violent muscle contractions).",
    "Red Flag Signs & Must-not-miss": "1. Ventricular Fibrillation (Low voltage AC) or Asystole (High voltage/DC).\n2. Compartment Syndrome: Due to deep tissue thermal damage.\n3. Delayed Neurological Deficits.\n4. Rhabdomyolysis / Myoglobinuria.\n5. Posterior Shoulder Dislocation (Classic after tetanic muscle contraction).",
    "Common Causes (Top 5)": "1. Household AC accidents.\n2. Lightning Strike.\n3. High-voltage Industrial accidents.\n4. Pediatric chewing of power cords.\n5. Arc burns.",
    "Key History": "1. Voltage level (>1000V is high-tension) and current type (AC is more dangerous).\n2. Path of current (Hand-to-hand is highest risk for cardiac arrest).\n3. Duration of contact and associated trauma (falls).",
    "Physical Exam": "1. Identify 'Entry' and 'Exit' wounds (Skin burns often underestimate internal damage).\n2. Neurovascular exam: Check for signs of compartment syndrome.\n3. Complete trauma survey.",
    "Tests & Purpose": "1. **ECG:** Mandatory for all electrical injuries (Identify arrhythmias).\n2. **CK / Urine Myoglobin:** Assess for internal muscle necrosis.\n3. **X-ray Views:**\n   - **C-spine:** AP, Lateral, Odontoid (Check for fracture from falls).\n   - **Shoulder:** AP, Scapular Y, Axillary (Check for posterior dislocation).\n4. **CT Brain:** If loss of consciousness or fall occurred.",
    "Management": "1. Aggressive IV Fluid Resuscitation (Maintain urine output >100mL/h if rhabdo is present).\n2. Wound care and Tetanus prophylaxis.\n3. Cardiac monitoring for at least 6-24 hours if high-risk.",
    "Consult & Disposition": "1. Burn Center / Trauma Surgery: For high-voltage or significant burns.\n2. Admission: For high-voltage, EKG changes, or signs of rhabdomyolysis.",
    "Discharge & Warning": "1. Discharge low-voltage (<240V) household injuries if ECG and exam are normal.\n2. Warning: Return for dark urine, numbness, or chest pain.",
    "Pearls & Pitfalls": "1. **Pearl:** Lightning causes 'Lichtenberg figures' (ferning pattern on skin) and often causes temporary 'Keraunoparalysis' (transient paralysis).\n2. **Pitfall:** Underestimating internal damage because skin burns look small."
  },
  {
    "Chief Complaint": "Near Drowning (Submersion Injury)",
    "Initial Action": "1. Immediate Oxygenation (Goal SpO2 >94%) and Airway management (Intubate if GCS <8).\n2. Remove wet clothing and initiate rewarming for hypothermia.\n3. Suctioning and gastric decompression.",
    "Red Flag Signs & Must-not-miss": "1. ARDS (Acute Respiratory Distress Syndrome).\n2. Non-cardiogenic Pulmonary Edema.\n3. Cerebral Edema and Anoxic Brain Injury.\n4. Secondary Hypothermia.\n5. Occult Trauma (C-spine injury from diving).",
    "Common Causes (Top 5)": "1. Swimming pool accidents (Pediatrics).\n2. Natural water exposure (Rivers/Ocean).\n3. Bathtub submersion (Infants/Elderly).\n4. Alcohol/Drug-related submersion.\n5. Diving-related trauma.",
    "Key History": "1. Submersion time and water temperature.\n2. Type of water (Fresh vs. Salt - though clinical treatment is similar).\n3. Associated events: Seizure, MI, or Trauma before submersion.\n4. CPR duration at the scene.",
    "Physical Exam": "1. Lung auscultation: Crackles, wheezing, or absent sounds.\n2. Neurological: GCS and pupillary response.\n3. Core temperature check.",
    "Tests & Purpose": "1. **ABG / VBG:** Assess for hypoxia and acidosis.\n2. **Chest X-ray:** Check for pulmonary edema or aspiration pneumonia (may be delayed).\n3. **Imaging Rules:**\n   - **NEXUS / Canadian C-spine Rules:** Essential for diving injuries.\n   - **CT Head:** If trauma or unexplained AMS.",
    "Management": "1. Aggressive Oxygenation (NIV/CPAP or Ventilator with PEEP).\n2. Rewarming for hypothermia.\n3. Supportive care for ARDS.",
    "Consult & Disposition": "1. ICU: For respiratory failure or required ventilation.\n2. Admission: For anyone with any respiratory symptoms or abnormal imaging.",
    "Discharge & Warning": "1. **6-Hour Observation:** Patients who are asymptomatic and have normal vitals/CXR after 6 hours may be discharged.\n2. Warning: Return for fever, cough, or difficulty breathing (Delayed 'dry drowning' effects).",
    "Pearls & Pitfalls": "1. **Pearl:** Prophylactic antibiotics and steroids are **not** recommended in the initial management of drowning.\n2. **Pitfall:** Discharging a patient too early; pulmonary edema can develop several hours after the event."
  },
  {
    "Chief Complaint": "Rash / 발진",
    "Initial Action": "1. Assess for Anaphylaxis: Look for SOB, hypotension, or tongue swelling.\n2. Identify 'Red Flag' morphology (Sloughing, Purpura, Bullae).\n3. Check for Mucosal involvement (Mouth, Eyes, Genitals).",
    "Red Flag Signs & Must-not-miss": "1. SJS / TEN: Mucosal sloughing + Nikolsky sign (Medical emergency).\n2. Meningococcemia: Non-blanching petechiae/purpura + Sepsis.\n3. Necrotizing Fasciitis: Redness + Extreme pain + Crepitus.\n4. Toxic Shock Syndrome: Diffuse erythroderma (Sunburn-like) + Shock.\n5. DRESS Syndrome: Rash + Eosinophilia + Systemic symptoms (Liver/Heart).",
    "Common Causes (Top 5)": "1. Urticaria / Allergic Reaction.\n2. Contact Dermatitis (Poison ivy, nickel).\n3. Viral Exanthems (Nonspecific).\n4. Cellulitis / Impetigo.\n5. Pityriasis Rosea.",
    "Key History": "1. New medications (Antibiotics, Anticonvulsants) in the last 2-8 weeks.\n2. Associated fever, sore throat, or joint pain.\n3. Travel history and insect bites (Lyme, Rocky Mountain Spotted Fever).\n4. Vaccination status.",
    "Physical Exam": "1. Morphology: Maculopapular, Vesicular, Bullous, or Purpuric.\n2. Distribution: Symmetrical vs. Asymmetrical; Trunk vs. Extremities.\n3. Nikolsky Sign: Gentle pressure causes epidermis to slough (Positive in TEN/SSSS).",
    "Tests & Purpose": "1. **CBC, CRP, LFTs:** Assess for systemic involvement (DRESS/Sepsis).\n2. **Blood Cultures:** If febrile or purpuric.\n3. **Skin Biopsy:** Rarely in ER, but essential for SJS/TEN diagnosis.",
    "Management": "1. Allergic/Urticaria: Antihistamines and Steroids.\n2. SJS/TEN: Immediate admission to Burn Unit; stop causative drug.\n3. Infection: Targeted antibiotics.",
    "Consult & Disposition": "1. Dermatology: For any life-threatening or uncertain rash.\n2. Burn Unit: For SJS/TEN.\n3. Discharge: For simple allergic or localized infectious rashes.",
    "Discharge & Warning": "1. Discharge with follow-up and 'rash diary'.\n2. Warning: Return for mouth sores, blisters, high fever, or difficulty breathing.",
    "Pearls & Pitfalls": "1. **Pearl:** If a rash is painful rather than itchy, think of serious conditions like Necrotizing Fasciitis or SJS.\n2. **Pitfall:** Missing mucosal involvement in a patient with a drug rash."
  },
  {
    "Chief Complaint": "Psychiatric Issues (SI / Behavioral Change)",
    "Initial Action": "1. **Safety First:** Secure the patient and environment; remove all dangerous objects (Search belongings).\n2. **Medical Clearance:** Rule out organic causes of behavioral change.\n3. Use physical or chemical restraints (e.g., Haloperidol, Midazolam) only if necessary for safety.",
    "Red Flag Signs & Must-not-miss": "1. Organic Brain Syndrome: AMS due to metabolic/infectious/toxic causes.\n2. Serotonin Syndrome / NMS: Autonomic instability + Rigidity.\n3. Acute Wernicke’s Encephalopathy.\n4. Delirium Tremens (Alcohol withdrawal).\n5. Acute Psychosis with command hallucinations.",
    "Common Causes (Top 5)": "1. Major Depressive Disorder (Suicidal Ideation).\n2. Substance Abuse / Intoxication.\n3. Schizophrenia (Acute Psychosis).\n4. Bipolar Disorder (Manic episode).\n5. Anxiety / Panic Attack.",
    "Key History": "1. Suicidal/Homicidal ideation, plan, and means.\n2. History of prior attempts (Strongest predictor).\n3. Recent substance use or withdrawal.\n4. Collateral history from family/police (Vital for behavioral changes).",
    "Physical Exam": "1. Thorough trauma check (Self-harm scars, hidden weapons).\n2. Neurological exam: Rule out focal deficits or ataxia (Organic signs).\n3. Vitals: Tachycardia/Hyperthermia (Sympathomimetic or NMS/Serotonin syndrome).",
    "Tests & Purpose": "1. **Medical Clearance Panel:** BST, Electrolytes, UA, Tox Screen, Ethanol level.\n2. **BUN/Cr & Ammonia:** If encephalopathy is suspected.\n3. **CT Brain:** For new-onset psychosis, trauma, or focal neuro signs.",
    "Management": "1. Constant 1:1 Observation (Sitter).\n2. Treat underlying medical issues first.\n3. De-escalation followed by pharmacotherapy for agitation.",
    "Consult & Disposition": "1. Psychiatry: For risk assessment and placement.\n2. Admission: To Psychiatric Unit for SI/Manic/Psychosis; Medical unit if not 'medically cleared'.",
    "Discharge & Warning": "1. Discharge only after Psychiatry clearance and ensuring a safety plan with family.\n2. Warning: Provide crisis hotline numbers and immediate return instructions if ideation recurs.",
    "Pearls & Pitfalls": "1. **Pearl:** Visual hallucinations are more common in organic/toxic causes; auditory hallucinations are more common in primary psychiatric disorders.\n2. **Pitfall:** Assuming 'behavioral change' is psychiatric in an elderly patient without ruling out a UTI or stroke."
  }
]

# ── 섹션 메타데이터 (아이콘, 색상) ───────────────────────────
SECTION_META = {
    "Initial Action": {
        "icon": "⚡",
        "label": "Initial Action",
        "color": "#1e40af",       # 파란색
        "bg": "#eff6ff",
        "border": "#3b82f6",
    },
    "Red Flag Signs & Must-not-miss": {
        "icon": "🚨",
        "label": "Must-not-miss",
        "color": "#991b1b",       # 빨간색
        "bg": "#fff1f2",
        "border": "#ef4444",
    },
    "Common Causes (Top 5)": {
        "icon": "📋",
        "label": "Common Causes",
        "color": "#92400e",       # 주황색
        "bg": "#fffbeb",
        "border": "#f59e0b",
    },
    "Key History": {
        "icon": "💬",
        "label": "Key History",
        "color": "#065f46",       # 초록색
        "bg": "#ecfdf5",
        "border": "#10b981",
    },
    "Physical Exam": {
        "icon": "🩺",
        "label": "Physical Exam",
        "color": "#1e3a5f",       # 네이비
        "bg": "#e0f2fe",
        "border": "#0ea5e9",
    },
    "Tests & Purpose": {
        "icon": "🔬",
        "label": "Tests",
        "color": "#4c1d95",       # 보라색
        "bg": "#f5f3ff",
        "border": "#8b5cf6",
    },
    "Management": {
        "icon": "💊",
        "label": "Management",
        "color": "#1e3a2f",       # 진초록
        "bg": "#dcfce7",
        "border": "#22c55e",
    },
    "Consult & Disposition": {
        "icon": "🏥",
        "label": "Consult & Disposition",
        "color": "#374151",       # 회색
        "bg": "#f9fafb",
        "border": "#6b7280",
    },
    "Discharge & Warning": {
        "icon": "⚠️",
        "label": "Discharge & Warning",
        "color": "#78350f",       # 갈색
        "bg": "#fef9c3",
        "border": "#eab308",
    },
    "Pearls & Pitfalls": {
        "icon": "💎",
        "label": "Pearls & Pitfalls",
        "color": "#312e81",       # 인디고
        "bg": "#eef2ff",
        "border": "#6366f1",
    },
}

SECTION_ORDER = list(SECTION_META.keys())

# ── 커스텀 CSS ────────────────────────────────────────────────
def inject_css():
    st.markdown(
        """
        <style>
        /* 구글 폰트 불러오기 */

        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;600;700;800&display=swap');

        /* 전체 앱에 폰트 적용 */

        html, body, [class*="css"] {

            font-family: 'Noto Sans KR', sans-serif !important;

        }
        
        /* 전체 배경 */
        [data-testid="stAppViewContainer"] {
            background-color: #0f172a;
        }
        [data-testid="stSidebar"] {
            background-color: #1e293b;
        }
        /* 메인 타이틀 */
        .main-title {
            font-size: 2rem;
            font-weight: 800;
            color: #f1f5f9;
            letter-spacing: -0.5px;
            margin-bottom: 0.2rem;
        }
        .main-subtitle {
            font-size: 0.9rem;
            color: #94a3b8;
            margin-bottom: 1.5rem;
        }
        /* 주호소 타이틀 배너 */
        .cc-banner {
            background: linear-gradient(135deg, #1d4ed8 0%, #0f172a 100%);
            border-radius: 12px;
            padding: 1.0rem 1.3rem;
            margin-bottom: 1.1rem;
        }
        .cc-banner h1 {
            color: #ffffff;
            font-size: 1.6rem;
            font-weight: 800;
            margin: 0;
        }
        .cc-banner p {
            color: #93c5fd;
            font-size: 0.82rem;
            margin: 0.3rem 0 0 0;
        }
        /* 섹션 카드 */
        .section-card {
            border-radius: 5px;
            padding: 0.6rem 0.9rem;
            margin-bottom: 0.55rem;
            border-left: 3px solid;
        }
        .section-card h4 {
            font-size: 1.05rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            margin: 0 0 0.6rem 0;
        }
        .section-card ul {
            margin: 0;
            padding-left: 1.0rem;
        }
        .section-card li {
            font-size: 0.88rem;
            line-height: 1.65;
            margin-bottom: 0.25rem;
        }
        /* 사이드바 검색창 */
        .sidebar-label {
            color: #94a3b8;
            font-size: 0.78rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.4rem;
        }
        /* 즐겨찾기 버튼 */
        .fav-chip {
            display: inline-block;
            background: #1e3a5f;
            color: #93c5fd;
            border-radius: 999px;
            padding: 0.25rem 0.75rem;
            font-size: 0.78rem;
            margin: 0.2rem 0.2rem 0 0;
            cursor: pointer;
        }
        /* 결과 없을 때 */
        .no-result {
            text-align: center;
            color: #64748b;
            font-size: 1rem;
            margin-top: 3rem;
        }
        /* 섹션 토글 체크박스 정렬 */
        div[data-testid="stCheckbox"] label {
            font-size: 0.82rem;
            color: #cbd5e1;
        }
                /* ── 사이드바 텍스트 전체 강제 밝은 색 ── */
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] div {
            color: #e2e8f0 !important;
        }
        /* 체크박스 라벨 */
        [data-testid="stSidebar"] div[data-testid="stCheckbox"] label p {
            color: #cbd5e1 !important;
        }
        /* 사이드바 입력창 */
        [data-testid="stSidebar"] input {
            color: #f1f5f9 !important;
            background-color: #334155 !important;
            border: 1px solid #475569 !important;
        }
        /* divider */
        [data-testid="stSidebar"] hr {
            border-color: #334155 !important;
        }
        /* caption */
        [data-testid="stSidebar"] small,
        [data-testid="stSidebar"] .stCaption {
            color: #64748b !important;
        }
        /* 즐겨찾기 버튼 */
        [data-testid="stSidebar"] button[kind="secondary"] {
            background-color: #1e3a5f !important;
            color: #93c5fd !important;
            border: 1px solid #3b82f6 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# ── 유틸: 텍스트 -> 리스트 변환 ──────────────────────────────
def text_to_list(text: str) -> list[str]:
    """번호 제거 후 항목 리스트 반환"""
    lines = []
    for line in text.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        # "1. " 형태 번호 제거
        if len(line) > 2 and line[0].isdigit() and line[1] in (".", ")"):
            line = line[2:].strip()
        elif len(line) > 3 and line[:2].isdigit() and line[2] in (".", ")"):
            line = line[3:].strip()
        lines.append(line)
    return lines

# ── 섹션 카드 렌더링 ──────────────────────────────────────────
def render_section(key: str, text: str):
    meta = SECTION_META.get(key, {})
    icon = meta.get("icon", "•")
    label = meta.get("label", key)
    color = meta.get("color", "#334155")
    bg = meta.get("bg", "#f8fafc")
    border = meta.get("border", "#94a3b8")

    items = text_to_list(text)
    items_html = "".join(f"<li>{item}</li>" for item in items)

    card_html = f"""
    <div class="section-card" style="background:{bg}; border-left-color:{border};">
        <h4 style="color:{color};">{icon} {label}</h4>
        <ul style="color:{color};">
            {items_html}
        </ul>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

# ── 검색 필터링 ───────────────────────────────────────────────
def search_data(query: str) -> list[dict]:
    if not query.strip():
        return DATA
    q = query.lower()
    results = []
    for item in DATA:
        # 주호소명 + 전체 텍스트 검색
        full_text = " ".join(str(v) for v in item.values()).lower()
        if q in full_text:
            results.append(item)
    return results

# ── 즐겨찾기 관리 ─────────────────────────────────────────────
def init_favorites():
    if "favorites" not in st.session_state:
        st.session_state.favorites = []

def toggle_favorite(cc_name: str):
    favs = st.session_state.favorites
    if cc_name in favs:
        favs.remove(cc_name)
    else:
        favs.append(cc_name)

# ── 메인 앱 ──────────────────────────────────────────────────
def main():
    inject_css()
    init_favorites()

    # ── 사이드바 ──────────────────────────────────────────────
    with st.sidebar:
        st.markdown(
            '<div class="main-title">🚨 ED Quick Ref</div>'
            '<div class="main-subtitle">Based on Tintinalli 9e · Rosen 10e</div>',
            unsafe_allow_html=True,
        )
        st.divider()

        # 검색창
        st.markdown('<div class="sidebar-label">🔍 Search Chief Complaint</div>', unsafe_allow_html=True)
        query = st.text_input(
            label="search",
            placeholder="e.g. fever, syncope, AMS...",
            label_visibility="collapsed",
        )

        st.divider()

        # 섹션 표시 토글
        st.markdown('<div class="sidebar-label">📌 Sections to Display</div>', unsafe_allow_html=True)
        visible_sections = {}
        # 2열로 배치
        col_a, col_b = st.columns(2)
        for i, key in enumerate(SECTION_ORDER):
            meta = SECTION_META[key]
            col = col_a if i % 2 == 0 else col_b
            with col:
                visible_sections[key] = st.checkbox(
                    f"{meta['icon']} {meta['label'].split('(')[0].strip()[:18]}",
                    value=True,
                    key=f"chk_{key}",
                )

        st.divider()

        # 즐겨찾기 목록
        st.markdown('<div class="sidebar-label">⭐ Favorites</div>', unsafe_allow_html=True)
        favs = st.session_state.favorites
        if favs:
            for fav in favs:
                if st.button(f"⭐ {fav}", key=f"fav_btn_{fav}", use_container_width=True):
                    query = fav  # 즐겨찾기 클릭 시 검색어로 사용
        else:
            st.caption("즐겨찾기가 없습니다.")

        st.divider()
        st.caption("💡 Tip: 섹션 체크박스로 원하는 항목만 볼 수 있습니다.")

    # ── 메인 영역 ─────────────────────────────────────────────
    results = search_data(query)

    if not results:
        st.markdown(
            '<div class="no-result">'
            "🔍 검색 결과가 없습니다.<br><small>다른 키워드로 검색해 보세요.</small>"
            "</div>",
            unsafe_allow_html=True,
        )
        return

    # 검색 결과 수 표시
    st.markdown(
        f"<p style='color:#64748b; font-size:0.82rem; margin-bottom:0.5rem;'>"
        f"검색 결과: <b style='color:#93c5fd;'>{len(results)}</b>개 항목</p>",
        unsafe_allow_html=True,
    )

    for item in results:
        cc = item["Chief Complaint"]

        # 주호소 배너
        is_fav = cc in st.session_state.favorites
        fav_icon = "⭐" if is_fav else "☆"

        col_title, col_fav = st.columns([11, 1])
        with col_title:
            st.markdown(
                f'<div class="cc-banner">'
                f'<h1>🏥 {cc}</h1>'
                f"</div>",
                unsafe_allow_html=True,
            )
        with col_fav:
            st.write("")
            st.write("")
            if st.button(fav_icon, key=f"fav_{cc}", help="즐겨찾기 추가/제거"):
                toggle_favorite(cc)
                st.rerun()

        # 섹션 렌더링 (2열 레이아웃)
        left_keys = SECTION_ORDER[:5]   # Initial Action ~ Physical Exam
        right_keys = SECTION_ORDER[5:]  # Tests ~ Pearls

        col_left, col_right = st.columns(2, gap="medium")

        with col_left:
            for key in left_keys:
                if visible_sections.get(key) and key in item:
                    render_section(key, item[key])

        with col_right:
            for key in right_keys:
                if visible_sections.get(key) and key in item:
                    render_section(key, item[key])

        st.divider()

if __name__ == "__main__":
    main()
