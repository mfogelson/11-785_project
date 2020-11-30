# 11-785_project
11-785 Group Project: YouShen Poetry generation

## Deliverables
* Project Proposal: https://www.overleaf.com/2953816942chzfyjrhfknh

* Midterm Report (Due 10-10-20): https://www.overleaf.com/2483957362fmgtfyvrxvpv
  - Instuctions: https://piazza.com/class/k9lk3ucwopisb?cid=1426

* Final Report (Due 11-27-20): TBD

## Key Resources
* Gwern Blog Poetry Learning with GPT2: https://www.gwern.net/GPT-2
  - Teaches how to run GPT2 
  - Suggestions for improvements
  - Experiments 

* Nshepperd/gpt-2 Github: https://github.com/nshepperd/gpt-2
  - Good documentation for running GPT2
  - How GPT2 Works

* Cole Peterson Master's Thesis: https://dspace.library.uvic.ca/bitstream/handle/1828/10801/Peterson_Cole_MSc_2019.pdf?sequence=3&isAllowed=y#Hfootnote.12
  - Useful information about poetry datasets
  - Other methods for learning Poetry 
  
* Ng Wai Foong's Medium Article: https://medium.com/ai-innovation/beginners-guide-to-retrain-gpt-2-117m-to-generate-custom-text-content-8bb5363d8b7f
  - Step by step for learning how to train GPT2 Model
  

## Data
* Raw Lymeric Data
https://raw.githubusercontent.com/sballas8/PoetRNN/master/data/limericks.csv

* cleaned Project Gutenberg samples (Gwern): https://www.gwern.net/docs/ai/2019-10-17-117m-poetry-cleanprojectgutenberg-samples.txt

* Poetry Foundation-finetuned samples (Gwern): https://www.gwern.net/docs/ai/2019-10-19-117m-poetryfoundation-samples.txt

## Models
* 117M-Clean (Gwern Model): https://mega.nz/#!2PhghaZD!_IJPpErXIRIDwRI0ktq2UKUZClDEoY7z8UpF28_qme8

* 117M-Clean-Lym **Note**:Model is too large to store on github contact Mitch to share
  - Train time: 21hrs
  - Loss: 0.9
  
* 117M-AA: **Note**:Model is too large to store on github contact Mitch to share
  - Train time: 40hrs
  - Loss: 0.11
  
* 117M-AABB: **Note**:Model is too large to store on github contact Mitch to share
  - Train time: 40hrs
  - Loss: 0.1
  
* 117M-limerick **Note**:Model is too large to store on github contact Mitch to share
  - Train time: 40hrs
  - Loss: 0.26
  
## Samples (Experiment1 Model) 
1:

    caboyola's a genus of weeds

    that grows near the shore and seeds seeds

    or these shrubs found beside

    are quite furry each side

    <|endoftext|>

2:

    a person who's often so rude

    takes a tack of a beach that's subdued

    in a business the lad

    is more childish than bad

    <|endoftext|>

3:

    an episcopal practice i'm told

    is quite certain to fight for our gold

    to get gold from the king

    to be saved from the thing

    <|endoftext|>

4:

    this is all about grandma who's proud

    of her years in society's crowd

    she has got a big raise

    in those fungal-type ways

    <|endoftext|>

## Experiment 1
Create corpus of limericks:
    
    [A |$| A]

    [B |$| B]

    [END]

Limericks Definition
* 5 Line Rhyming Poem
* Rhyming Structure: A A B B A

Raw Data Example:

    cap'n jack was washed over the side.

    his crew searched but found not hair nor hide.

    no longer the helm,

    but the deep benthic realm,

    is where jack will forever reside.

Processed Data Output:

    ["cap'n jack was washed over the side|$|his crew searched but found not hair nor hide"]

    ['no longer the helm|$|but the deep benthic realm']

    ['<|endoftext|>']

## Files Included
- preprocesser.ipynb -> Jupyter Notebook for preprocessing raw data

- rhyming_evaluation.ipynb -> Jupyter Notebook to evaluate output samples Rhyming Success


## How to move forward?

1. Better preprocessing data now that we know how the GPT2 matches structure of input - Xinkai

2. Finding ways to evaluate outputs quantitatively
    * Rhyming - Chris
    * Non-sense words - Mitch
    * Pronoun reference - Tony
    * Action reference

3. Change GPT2
    * Loss Function
    * NOTE: Cannot be done until non-human quantitative evaluation methods are made 
    

---
### PS: Setting up HTTP Access on EC2 instances:

Update:

Alright, I just figured out that some steps were not needed at all. Should be really simple.

Some details:

1. Launch instances
    * Amazon Linux 2 AMI (HVM), SSD Volume Type - ami-03657b56516ab7912 (64-bit x86) / ami-023b120e01f4779c1 (64-bit Arm)

    (The first one in the free tier group)
    
    (Note that the username is ec2-user instead of ubuntu)
        
    (Not recommended because many libraries (including pip, flask) need manual installation)

    (Install pip:)
    ```
    $ curl -O https://bootstrap.pypa.io/get-pip.py
    $ python get-pip.py --user
    ```
    (Probably need to install python3 later for our project???)
    
2. On the Configure Security Group page
    * Add Rule "Custom TCP Rule", where the Port Range must cover the port number used by our web app
    * The source IP can be set to "0.0.0.0/0, ::/0" just for now

3. In app.py
    * The listening IP should be set to brodcast IP address, i.e. "0.0.0.0"


