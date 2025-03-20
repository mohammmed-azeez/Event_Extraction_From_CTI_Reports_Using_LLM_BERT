#!/usr/bin/env python3
"""
Generate synthetic data for the Event Extraction from CTI Reports project.
This script creates synthetic sentences with labels in the same format as the sample data.
"""

import random
import os
from itertools import combinations

# Templates for generating synthetic sentences
TEMPLATES = {
    "AttackDatabreach": [
        "Hackers {verb} access to {target}'s database and stole {data_type}.",
        "The data breach at {target} exposed {data_type} of {number} {users}.",
        "{actor} breached {target}'s systems and exfiltrated {data_type}.",
        "A sophisticated attack on {target} resulted in the theft of {data_type}.",
        "{target} confirmed that {actor} had accessed {data_type} in a breach discovered on {date}.",
    ],
    "AttackPhishing": [
        "A phishing campaign targeted {target} with emails that appeared to come from {spoofed_sender}.",
        "{actor} launched a spear-phishing attack against {target} using {lure}.",
        "Employees at {target} received phishing emails containing {malicious_content}.",
        "The phishing attack used {technique} to trick users into revealing their {credentials}.",
        "{target} warned its {users} about a phishing campaign that mimics {spoofed_sender}.",
    ],
    "AttackRansom": [
        "The ransomware attack encrypted all files on {target}'s {systems} and demanded {amount} for the decryption key.",
        "{actor} deployed ransomware that affected {target}'s operations for {duration}.",
        "A new ransomware variant targeted {target}, encrypting {data_type} and demanding payment.",
        "{target} was hit by ransomware that not only encrypted files but also threatened to leak {data_type}.",
        "The {ransomware_name} ransomware attack forced {target} to shut down {systems} for {duration}.",
    ],
    "DiscoverVulnerability": [
        "Security researchers discovered a {severity} vulnerability in {software} that could allow {impact}.",
        "A {severity} flaw was found in {software} that could be exploited to {impact}.",
        "Researchers at {security_firm} identified a vulnerability in {software} affecting versions {versions}.",
        "A {vulnerability_type} vulnerability was discovered in {software} that could lead to {impact}.",
        "{security_firm} reported a previously unknown vulnerability in {software} that allows attackers to {impact}.",
    ],
    "PatchVulnerability": [
        "{vendor} released a patch to fix the {severity} security vulnerability in {software}.",
        "A security update was issued by {vendor} to address the vulnerability in {software}.",
        "{vendor} has patched {number} vulnerabilities in its {software} product, including a {severity} flaw.",
        "The latest update for {software} includes fixes for {number} security issues discovered by {security_firm}.",
        "Users of {software} are urged to update to version {version} which patches a {severity} security flaw.",
    ],
    "O": [
        "The cybersecurity firm released a detailed report about the attack campaign.",
        "Experts recommend implementing multi-factor authentication to enhance security.",
        "The company hired external security consultants to improve their security posture.",
        "The threat intelligence report provides insights into the tactics used by the threat actor.",
        "Security teams are advised to monitor for indicators of compromise in their networks.",
    ]
}

# Variables to fill in the templates
VARIABLES = {
    "verb": ["gained", "obtained", "acquired", "compromised"],
    "target": ["a healthcare provider", "a financial institution", "a government agency", "a technology company", "a university", "a retail chain", "a manufacturing firm"],
    "data_type": ["personal information", "credit card details", "login credentials", "medical records", "financial data", "intellectual property", "customer records", "employee information"],
    "number": ["thousands", "millions", "hundreds of thousands", "an undisclosed number", "approximately 100,000", "over a million"],
    "users": ["customers", "users", "patients", "clients", "employees", "students"],
    "actor": ["a state-sponsored group", "cybercriminals", "an advanced persistent threat (APT) group", "hackers", "a ransomware gang", "unknown attackers", "a threat actor"],
    "date": ["January 2023", "February 2023", "March 2023", "April 2023", "May 2023", "June 2023"],
    "spoofed_sender": ["the IT department", "a trusted vendor", "the HR department", "the CEO", "a financial institution", "a government agency"],
    "lure": ["fake invoice attachments", "COVID-19 information", "job offers", "security alerts", "password reset requests"],
    "malicious_content": ["malicious attachments", "links to fake login pages", "macro-enabled documents", "malware downloads"],
    "technique": ["social engineering", "urgency tactics", "impersonation", "business email compromise", "fake login pages"],
    "credentials": ["login credentials", "personal information", "financial details", "authentication tokens"],
    "systems": ["servers", "workstations", "network infrastructure", "cloud services", "databases", "operational technology"],
    "amount": ["$100,000 in Bitcoin", "$500,000 in cryptocurrency", "millions in ransom", "a six-figure sum", "an undisclosed amount"],
    "duration": ["several days", "a week", "over a month", "48 hours", "several weeks"],
    "ransomware_name": ["Ryuk", "Conti", "REvil", "LockBit", "BlackCat", "DarkSide", "WannaCry"],
    "severity": ["critical", "high-severity", "zero-day", "serious", "remote code execution", "privilege escalation"],
    "software": ["Windows", "Apache", "WordPress", "iOS", "Android", "Linux kernel", "Chrome", "Firefox", "Microsoft Exchange", "Cisco routers", "VMware ESXi"],
    "impact": ["remote code execution", "privilege escalation", "data theft", "unauthorized access", "complete system compromise", "lateral movement"],
    "security_firm": ["Google Project Zero", "Microsoft Threat Intelligence", "Mandiant", "CrowdStrike", "Kaspersky Lab", "ESET", "Symantec"],
    "vulnerability_type": ["buffer overflow", "SQL injection", "cross-site scripting", "authentication bypass", "path traversal", "command injection"],
    "versions": ["3.x through 4.2", "all versions prior to 2.5.3", "versions released before January 2023", "the latest release", "LTS versions"],
    "vendor": ["Microsoft", "Apple", "Google", "Oracle", "Adobe", "Cisco", "VMware", "IBM"],
    "version": ["2.5.3", "4.2.1", "7.0.5", "10.3.4", "2023.1.2"]
}

def fill_template(template, variables):
    """Fill in a template with random variables."""
    for var_name, var_values in variables.items():
        if "{" + var_name + "}" in template:
            template = template.replace("{" + var_name + "}", random.choice(var_values))
    return template

def generate_sentence(label):
    """Generate a sentence for a given label."""
    template = random.choice(TEMPLATES[label])
    return fill_template(template, VARIABLES)

def generate_multi_label_sentence(labels):
    """Generate a sentence that fits multiple labels."""
    # For simplicity, we'll just combine templates from each label
    # In a real scenario, you'd want more sophisticated sentence generation for multi-label cases
    primary_label = random.choice(labels)
    sentence = generate_sentence(primary_label)
    
    # Add context from other labels to make it a multi-label sentence
    for label in labels:
        if label != primary_label:
            # Add a phrase from this label's domain
            additional_context = " " + random.choice([
                f"This occurred after {generate_sentence(label).lower()}",
                f"Additionally, {generate_sentence(label).lower()}",
                f"The attack also involved {generate_sentence(label).lower()}"
            ])
            sentence += additional_context
            break  # Just add one additional context to keep sentences reasonable
            
    return sentence

def generate_data(num_samples=1000, output_file="synthetic_data.txt"):
    """Generate synthetic data and write to a file."""
    labels = ["AttackDatabreach", "AttackPhishing", "AttackRansom", "DiscoverVulnerability", "PatchVulnerability", "O"]
    
    # Probability distribution for single labels vs multi-labels
    # 80% single label, 20% multi-label
    single_label_prob = 0.8
    
    with open(output_file, 'w') as f:
        for _ in range(num_samples):
            if random.random() < single_label_prob:
                # Generate single-label sentence
                label = random.choice(labels)
                sentence = generate_sentence(label)
                f.write(f"{sentence}|{label}\n")
            else:
                # Generate multi-label sentence (2-3 labels)
                num_labels = random.randint(2, 3)
                selected_labels = random.sample([l for l in labels if l != "O"], num_labels)  # Don't include "O" in multi-label
                sentence = generate_multi_label_sentence(selected_labels)
                f.write(f"{sentence}|{', '.join(selected_labels)}\n")
    
    print(f"Generated {num_samples} synthetic data samples in {output_file}")

if __name__ == "__main__":
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    # Generate synthetic data
    generate_data(num_samples=1000, output_file="data/synthetic_data.txt")
    
    print("Synthetic data generation complete.")
    print("The data is in the format: 'sentence|label' or 'sentence|label1, label2'")
    print("You can use this data with the main.ipynb notebook for training and testing.")