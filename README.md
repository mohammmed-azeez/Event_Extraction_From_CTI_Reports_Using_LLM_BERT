# Event-Extraction-from-Cyber-Threat-Report-Using-BERT-Model

The original dataset is from [Ebiquity/CASIE](https://github.com/Ebiquity/CASIE),
We have meticulously relabeled all the data and converted it to a sentence-level task. This new dataset is also being utilized for other cybersecurity classification tasks.

My research has been submitted to the Cryptology and Information Security Conference 2024. We will update this README file once we receive confirmation of acceptance from the conference.

Thank you for your interest in My work.

## Please give the star for this repo

If you only directly using a part of code of this repo, please give me star >//<

## Data

### Dataset Description

The dataset used in this project is derived from the [Ebiquity/CASIE](https://github.com/Ebiquity/CASIE) dataset, which has been relabeled and converted to a sentence-level task. The dataset contains sentences from cyber threat intelligence reports labeled with one or more of the following event types:

- **AttackDatabreach**: Events related to data breaches where sensitive information is accessed or stolen
- **AttackPhishing**: Events related to phishing attacks
- **AttackRansom**: Events related to ransomware attacks
- **DiscoverVulnerability**: Events related to the discovery of security vulnerabilities
- **PatchVulnerability**: Events related to patching or fixing security vulnerabilities
- **O**: Other sentences that don't describe any of the above events

### Data Format

The data is stored in text files with each line containing a sentence and its corresponding label(s) separated by a pipe character (`|`). Multiple labels are separated by commas. For example:

```
The ransomware attack encrypted all files on the company's servers.|AttackRansom
Security researchers discovered a critical vulnerability in the software.|DiscoverVulnerability
Multiple attackers exploited the vulnerability to steal data and deploy ransomware.|AttackDatabreach, AttackRansom
```

### Sample Data

This repository includes sample data files in the `data` directory to demonstrate the format and content of the dataset. These files contain examples of each event type and can be used to test the code in this repository.

To use the full dataset, you would need to:

1. Create a `data` directory in the root of the project (if it doesn't exist)
2. Place your text files with the proper format in the `data` directory
3. Run the code in `main.ipynb` to process the data and train the model

### Data Statistics

The complete dataset contains approximately 17,269 labeled sentences with the following distribution:

- AttackDatabreach: ~1,571 instances
- AttackPhishing: ~1,374 instances
- AttackRansom: ~1,581 instances
- DiscoverVulnerability: ~1,771 instances
- PatchVulnerability: ~1,228 instances
- O (Other): ~10,209 instances

Some sentences have multiple labels, as they describe multiple types of events.

### Synthetic Data Generation

This repository includes a script to generate synthetic data for experimentation and testing. The script creates sentences with labels in the same format as the real dataset.

To generate synthetic data:

1. Run the script:
   ```bash
   python generate_synthetic_data.py
   ```

2. This will create a file `data/synthetic_data.txt` with 1000 synthetic samples.

3. You can modify the script to generate more samples or customize the templates used for sentence generation.

The synthetic data is not meant to replace the real dataset but can be useful for:
- Testing the code and model pipeline
- Experimenting with different model configurations
- Understanding the data format and structure
- Augmenting the real dataset for training

Note that the synthetic data is generated using templates and may not capture all the nuances and complexity of real cyber threat intelligence reports.
