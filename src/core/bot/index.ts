import { Bot } from 'grammy'
import { BOT_TOKEN } from '../../utils/env'

export const bot = new Bot(BOT_TOKEN)

const emojies: { [key: string]: string } = {
	// Happy/Positive
	smile: '😂',
	خنده: '😂',
	happy: '😊',
	خوشحال: '😊',
	joy: '😄',
	شادی: '😄',
	laugh: '🤣',
	قهقهه: '🤣',
	grin: '😁',
	پوزخند: '😁',

	// Sad/Negative
	sad: '🥲',
	غمگین: '🥲',
	cry: '😢',
	گریه: '😢',
	tears: '😭',
	اشک: '😭',
	disappointed: '😞',
	ناامید: '😞',
	worried: '😟',
	نگران: '😟',

	// Love/Heart
	heart: '❤️',
	قلب: '❤️',
	love: '😍',
	عشق: '😍',
	kiss: '😘',
	بوس: '😘',
	hearteyes: '😍',
	عاشق: '😍',

	// Anger/Frustrated
	angry: '😠',
	عصبانی: '😠',
	rage: '😡',
	خشم: '😡',
	mad: '🤬',
	دیوانه: '🤬',

	// Surprise/Shock
	surprise: '😲',
	تعجب: '😲',
	shock: '😱',
	شوک: '😱',
	wow: '😮',
	واو: '😮',

	// Cool/Confident
	cool: '😎',
	باحال: '😎',
	sunglasses: '😎',
	عینکی: '😎',
	wink: '😉',
	چشمک: '😉',

	// Thinking/Confused
	thinking: '🤔',
	فکر: '🤔',
	confused: '😕',
	گیج: '😕',

	// Tired/Sick
	tired: '😴',
	خسته: '😴',
	sick: '🤒',
	بیمار: '🤒',
	fever: '🤒',
	تب: '🤒',

	// Gestures
	thumbsup: '👍',
	لایک: '👍',
	thumbsdown: '👎',
	دیسلایک: '👎',
	ok: '👌',
	اوکی: '👌',
	peace: '✌️',
	صلح: '✌️',
	clap: '👏',
	تشویق: '👏',

	// // Animals
	// cat: '🐱',
	// گربه: '🐱',
	// dog: '🐶',
	// سگ: '🐶',
	// lion: '🦁',
	// شیر: '🦁',
	// tiger: '🐅',
	// ببر: '🐅',
	//
	// // Food
	// pizza: '🍕',
	// پیتزا: '🍕',
	// burger: '🍔',
	// همبرگر: '🍔',
	// coffee: '☕',
	// قهوه: '☕',
	// tea: '🍵',
	// چای: '🍵',

	// Objects
	fire: '🔥',
	آتش: '🔥',
	star: '⭐',
	ستاره: '⭐',
	moon: '🌙',
	ماه: '🌙',
	sun: '☀️',
	خورشید: '☀️',

	// Sports
	football: '⚽',
	فوتبال: '⚽',
	basketball: '🏀',
	بسکتبال: '🏀',

	// Weather
	rain: '🌧️',
	باران: '🌧️',
	snow: '❄️',
	برف: '❄️',
	thunder: '⛈️',
	رعد: '⛈️',

	// Party/Celebration
	party: '🎉',
	جشن: '🎉',
	cake: '🎂',
	کیک: '🎂',
	gift: '🎁',
	هدیه: '🎁',

	// Technology
	phone: '📱',
	تلفن: '📱',
	computer: '💻',
	کامپیوتر: '💻',

	// Money
	money: '💰',
	پول: '💰',
	dollar: '💵',
	دلار: '💵',

	// Time
	clock: '🕐',
	ساعت: '🕐',

	// Transportation
	car: '🚗',
	ماشین: '🚗',
	plane: '✈️',
	هواپیما: '✈️',

	// Flowers/Nature
	flower: '🌸',
	گل: '🌸',
	rose: '🌹',
	رز: '🌹',
	tree: '🌳',
	درخت: '🌳',
}

bot.command('start', (ctx) => ctx.reply('Welcome!'))

bot.on('inline_query', async (ctx) => {
	const message = ctx.inlineQuery.query.trim()

	for (const key in emojies) {
		if (message.startsWith(key)) {
			let mult = 1
			let emoji = emojies[key]

			// Find dot and extract number part with optimized Persian/English number handling
			const dot = message.indexOf('.')
			if (dot !== -1) {
				const numb = message.substring(dot + 1).trim()

				// Direct conversion without full string processing
				let num = 0
				for (let i = 0; i < numb.length; i++) {
					const char = numb[i]
					let digit: number

					if (char >= '0' && char <= '9') {
						// English digits
						digit = char.charCodeAt(0) - '0'.charCodeAt(0)
					} else if (char >= '۰' && char <= '۹') {
						// Persian digits
						digit = char.charCodeAt(0) - '۰'.charCodeAt(0)
					} else {
						// Stop at first non-digit character
						break
					}

					num = num * 10 + digit
				}

				if (num > 0) mult = num
			}

			const result = emoji.repeat(mult)

			const results = [
				{
					type: 'article' as const,
					id: `${key}_${mult}`,
					title: result,
					description: '',
					input_message_content: {
						message_text: result,
					},
				},
			]

			await ctx.answerInlineQuery(results)
			return
		}
	}

	await ctx.answerInlineQuery([])
})

export default bot
