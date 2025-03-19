# Movie Data Processing and Clustering Pipeline

This project implements a data processing and clustering pipeline using Docker and Python. It leverages K-means clustering on movie data and provides insights through Exploratory Data Analysis (EDA) and visualization.

## Project Structure

The pipeline is structured as follows:

1. **Data Loading (`load.py`)**: Loads the movie dataset.
2. **Data Preprocessing (`dpre.py`)**: Cleans and preprocesses the data.
3. **Exploratory Data Analysis (`eda.py`)**: Generates three textual insights.
4. **Visualization (`vis.py`)**: Creates a scatter plot visualization.
5. **Clustering Model (`model.py`)**: Applies K-means clustering to the data.

The pipeline automatically executes each step in the correct order, from data loading to clustering.

---

## Prerequisites

- Docker installed on your system.
- Python 3.x installed inside the Docker container.
- Required Python libraries:
  - `pandas`
  - `scikit-learn`
  - `matplotlib`

---

## Building and Running the Docker Container

### Step 1: Build the Docker Image

Build the Docker image using the following command:

```bash
docker build -t bd-a1-image .
```

### Step 2: Run the Docker Container

Start the container:

```bash
docker run -it --name hish bd-a1-image bash
```

### Step 3: Navigating Inside the Container

Once inside the container, navigate to the project directory:

```bash
cd /home/doc-bd-a1
```

### Step 4: Exit the container

```bash
exit
```

### Step 5: Copy Python Files from Host to Container

To copy the Python files to the container, use the following commands:

```bash
docker cp load.py hish:/home/doc-bd-a1
docker cp dpre.py hish:/home/doc-bd-a1
docker cp eda.py hish:/home/doc-bd-a1
docker cp vis.py hish:/home/doc-bd-a1
docker cp model.py hish:/home/doc-bd-a1
docker cp '.\top_rated_movies(tmdb).csv' hish:/home/doc-bd-a1
```

### Step 6: Run the container again

```bash
docker start hish
docker exec -it hish bash
```

### Step 7: Open Bash and Run the Script

Open the Bash terminal inside the container and run the initial script to start the entire pipeline:

```bash
python3 load.py top_rated_movies\(tmdb\).csv
```

---

## Output Files

The following output files will be generated during the pipeline execution:

- **EDA Insights:**

  - `eda-in-1.txt`: Average rating per year.
  - `eda-in-2.txt`: Top 10 movies by popularity.
  - `eda-in-3.txt`: Number of movies per rating category.

- **Visualization:**

  - `vis.png`: Scatter plot of popularity vs. vote average.

- **Clustering:**
  - `k.txt`: Number of records per cluster.

### Step 8: Verifying Output Files

To check the output files, list the contents of the working directory:

```bash
ls -lh
```

To view the content of each file:

```bash
cat eda-in-1.txt
cat eda-in-2.txt
cat eda-in-3.txt
cat k.txt
```

### Step 9: Run the script using Git Bash or WSL

To run using Git Bash, open it then navigate to the directory containing the final.sh script and run:

```bash
bash ./final.sh
```

---

## Cleaning Up

To stop and remove the container after execution:

```bash
docker stop hish
docker rm hish
```

To remove the Docker image:

```bash
docker rmi bd-a1-image
```

To delete all generated output files:

```bash
rm -f *.txt *.png
```

---

## Troubleshooting

- If the container fails to start, make sure that the image has been built correctly.
- To rebuild the image after making changes, use:
  ```bash
  docker build --no-cache -t bd-a1-image .
  ```
- If you encounter permission issues, try running Docker with `sudo`.
