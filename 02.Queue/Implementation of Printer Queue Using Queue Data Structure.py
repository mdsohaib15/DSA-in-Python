'''
 Apply Queue data structure for a printer queue, print jobs are processed in the order they are received-first come, first served. New print jobs are added to the end of the queue, and the printer processes jobs from the front of the queue. Express the importance of using this type of data structure. 
'''
class PrinterQueue:
    def __init__(self):
        self.queue = []  # Initialize an empty list to represent the queue

    # Add a new print job to the end of the queue
    def add_job(self, job_name):
        self.queue.append(job_name)
        print(f"Print job '{job_name}' added to the queue.")

    # Process the next job in the queue (FIFO)
    def process_job(self):
        if not self.queue:  # Check if the queue is empty
            print("No print jobs in the queue.")
            return
        job_name = self.queue.pop(0)  # Remove and return the job at the front
        print(f"Processing print job: {job_name}")

    # Display all pending print jobs
    def display_jobs(self):
        if not self.queue:
            print("No pending print jobs.")
        else:
            print("Pending Print Jobs:")
            for i, job in enumerate(self.queue, start=1):
                print(f"{i}. {job}")


printer_queue = PrinterQueue()

# Adding jobs to the queue
printer_queue.add_job("Document1.pdf")
printer_queue.add_job("Photo.jpg")
printer_queue.add_job("Presentation.pptx")

# Display pending jobs
print("\nCurrent Printer Queue:")
printer_queue.display_jobs()

# Process jobs
print("\nProcessing Jobs:")
printer_queue.process_job()
printer_queue.process_job()

# Display pending jobs after processing
print("\nUpdated Printer Queue:")
printer_queue.display_jobs()
