import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_API_KEY });

// Starts an Actor and waits for it to finish
const username = "apify";
const actorName = "website-content-crawler";
const apa_url = "https://www.apa.org/depression-guideline/case-examples";
const wiley_url = "https://onlinelibrary.wiley.com/doi/10.1002/da.20457"
const { defaultDatasetId } = await client
    .actor(`${username}/${actorName}`)
    .call({
        "debugMode": false,
        "proxyConfiguration": {
            "useApifyProxy": true
        },
        "saveHtml": false,
        "saveMarkdown": false,
        "saveScreenshots": false,
        "startUrls": [{ url: apa_url }, { url: wiley_url }],
        "maxCrawlDepth": 5,
        "requestTimeoutSecs": 60,
        "respectRobotsTxt": false,
    });

// Lists items from the Actor's dataset
const { items } = await client.dataset(defaultDatasetId).listItems();

console.log('Items from the dataset:', JSON.stringify(items, null, 2));
