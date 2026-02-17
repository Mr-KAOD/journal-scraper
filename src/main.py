import asyncio
import os
from data_extraction.scimago_extractor import ScimagoExtractor

async def main():
    # Save CSV 
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    save_path = os.path.join(base_path, "data", "raw")
    
    print("=" * 5, "JOURNAL WEB SCRAPER", "=" * 5)
    query = input("Enter the keyword (e.g. cancer): ")
    
    extractor = ScimagoExtractor()
    
    try:
        df = await extractor.run_search_extraction(search_query=query, limit=10)
        
        if not df.empty:
            file_name = f"homepages_{query.replace(' ', '_')}.csv"
            full_route = os.path.join(save_path, file_name)
            
            df.to_csv(full_route, index=False)
            print(f"\n File saved successfully")
            print(df[["Journal", "Official Home"]])
        else:
            print("No results were found")
            
    except Exception as e:
        print(f"\n Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())