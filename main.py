import os
import typer
from pathlib import Path
from typing import Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from processor import process_exr_to_proxy

app = typer.Typer()

@app.command()
def main(
    input: Path = typer.Option(..., "--input", "-i", help="Input folder for EXR processing"),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Output folder (defaults to 'input folder/proxy<proxy_scale>')"),
    proxy_scale: float = typer.Option(0.5, "--proxy_scale", "-s", help="Resolution scale of output frames"),
    img_format: str = typer.Option("png", "--img_format", "-f", help="Output format of frames"),
    threads: int = typer.Option(5, "--threads", "-t", help="Max threads to use (defaults to 5)")
):
    """
    Process EXR files from the input folder, convert them to proxy files at the specified scale,
    and save them to the output folder in the specified image format.
    """
    if output is None:
        output = f"{input}/proxy_{proxy_scale}"

    output = Path(output)
    if not output.exists():
        output.mkdir(parents=True)
    
    exr_files = list(input.glob("*.exr"))
    max_threads = threads
    
    print(f"Using {max_threads} of {os.cpu_count()} total threads. (Change with -t )")

    if len(exr_files) == 0:
        print ("No EXR files in directory.")
        return
    
    try:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            with tqdm(total=len(exr_files)) as pbar:
                def update_progress():
                    pbar.update(1)
                
                futures = [
                    executor.submit(process_exr_to_proxy, exr_file, output, proxy_scale, img_format, update_progress)
                    for exr_file in exr_files
                ]
                
                for future in as_completed(futures):
                    future.result()
    except KeyboardInterrupt:
        print("Process interrupted by user. Shutting down...")
        executor.shutdown(wait=False, cancel_futures=True)
    else:
        typer.echo(f"Processed {len(exr_files)} EXR files.")

if __name__ == "__main__":
    app()
