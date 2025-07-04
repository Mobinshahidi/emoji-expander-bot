export const BOT_TOKEN = process.env.BOT_TOKEN!

if (!BOT_TOKEN) {
	throw new Error('BOT_TOKEN environment variable is required')
}
